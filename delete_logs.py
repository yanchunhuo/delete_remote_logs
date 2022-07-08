#
# delete_logs.py
# @author yanchunhuo
# @description 
# @created 2022-06-17T19:52:23.166Z+08:00
# @last-modified 2022-07-08T17:41:12.746Z+08:00
# github https://github.com/yanchunhuo
from common.dateTimeTool import DateTimeTool
from common.sshClient import SSHClient
from ruamel import yaml
import re

class Delete_Logs:
    def __init__(self,specify_host:str=None) -> None:
        self.specify_host=specify_host
        self.env_info=yaml.safe_load(open('config/env_info.yaml','r',encoding='utf-8'))
        self.servers_log_info=yaml.safe_load_all(open('config/servers_log_info.yaml','r',encoding='utf-8'))
        
    def run(self):
        if self.specify_host:
            for server_log_info in self.servers_log_info:
                if self.specify_host==server_log_info['host']:
                    self._delete_log(server_log_info)
                    break
        else:
            for server_log_info in self.servers_log_info:
                self._delete_log(server_log_info)
                
    def _delete_log(self,server_log_info:dict):
        host=server_log_info['host']
        username=server_log_info['username']
        password=server_log_info['password']
        pkey_file=self.env_info['private_key_file_path']
        # 连接服务器
        if server_log_info['password']:
            print('%s 连接【%s】主机，username【%s】password【%s】'%(DateTimeTool.getNowTime(),host,username,password))
            sshClient=SSHClient(ip=host,username=username,password=password)
        else:
            print('%s 连接【%s】主机，username【%s】pkey_file【%s】'%(DateTimeTool.getNowTime(),host,username,pkey_file))
            sshClient=SSHClient(ip=host,username=username,pkey_file=pkey_file)
        for del_log in server_log_info['del_logs']:
            is_del_dir=del_log['is_del_dir']
            del_type=del_log['del_type']
            del_how_day_ago=del_log['del_how_day_ago']
            file_path=del_log['file_path']
            filename_suf=del_log['filename_suf']
            if is_del_dir:
                print('%s 开始删除【%s】目录的日志'%(DateTimeTool.getNowTime(),file_path))
                self._delete_dir_log(sshClient=sshClient,del_type=del_type,del_how_day_ago=del_how_day_ago,file_path=file_path,filename_suf=filename_suf)
            else:
                print('%s 开始删除【%s】日志'%(DateTimeTool.getNowTime(),del_log['file_path']))
                self._delete_file_log(sshClient=sshClient,del_type=del_type,del_how_day_ago=del_how_day_ago,file_path=file_path)
                
    def _delete_dir_log(self,sshClient,del_type:int,del_how_day_ago:int,file_path:str,filename_suf:str):
        log_file_paths=[]
        self._get_dir_all_meet_condition_log_file_paths(sshClient=sshClient,log_file_paths=log_file_paths,dir_path=file_path,filename_suf=filename_suf)
        for log_file_path in log_file_paths:
            self._delete_file_log(sshClient=sshClient,del_type=del_type,del_how_day_ago=del_how_day_ago,file_path=log_file_path)
        
    def _get_dir_all_meet_condition_log_file_paths(self,sshClient,log_file_paths:list,dir_path:str,filename_suf:str):
        if not dir_path.endswith('/'):
            dir_path+='/'
        # 对路径或文件名包含空格的进行特殊处理
        get_file_names_command='ls %s'%dir_path.replace(' ','\ ')
        stdin, stdout, stderr, exit_code=sshClient.ssh_exec_command(get_file_names_command)
        file_names=stdout.readlines()
        for file_name in file_names:
            file_name=file_name.strip()
            file_path=(dir_path+file_name)
            # 对路径或文件名包含空格的进行特殊处理
            file_type_command='stat -c %%F %s'%file_path.replace(' ','\ ')
            stdin, stdout, stderr, exit_code=sshClient.ssh_exec_command(file_type_command)
            file_type=stdout.read().decode('utf-8').strip()
            if not 'directory'==file_type and file_type in ['regular empty file','regular file','symbolic link']:
                pattern='.*%s$'%filename_suf
                is_match=re.match(pattern,file_path)
                if file_path.endswith(filename_suf):
                    log_file_paths.append(file_path)
                elif is_match:
                    log_file_paths.append(file_path)
            else:
                self._get_dir_all_meet_condition_log_file_paths(sshClient=sshClient,log_file_paths=log_file_paths,dir_path=file_path,filename_suf=filename_suf)
    
    def _delete_file_log(self,sshClient,del_type:int,del_how_day_ago:int,file_path:str):
        if del_type==0:
            delete_command='>%s'%file_path.replace(' ','\ ')
        elif del_type==1:
            delete_command='rm -rf %s'%file_path.replace(' ','\ ')
        else:
            return
        # 判断是否需要删除几天前的日志，满足才删除
        if not del_how_day_ago==-1:
            get_file_last_modify_date_command='stat -c %%y %s'%file_path.replace(' ','\ ')
            stdin, stdout, stderr, exit_code=sshClient.ssh_exec_command(get_file_last_modify_date_command)
            last_modify_date=stdout.read().decode('utf-8')
            last_modify_date=last_modify_date[:19]
            last_modify_date=DateTimeTool.strToDateTime(last_modify_date)
            now_time=DateTimeTool.strToDateTime(DateTimeTool.getNowTime())
            days=(now_time-last_modify_date).days
            if days>=del_how_day_ago:
                stdin, stdout, stderr, exit_code=sshClient.ssh_exec_command(delete_command)
                if exit_code==0:
                    print('%s 删除【%s】日志成功...'%(DateTimeTool.getNowTime(),file_path))
                else:
                    print('%s 删除【%s】日志失败...%s'%(DateTimeTool.getNowTime(),file_path,stderr.read()))
            else:
                print('%s 当前【%s】日志不满足删除条件，无需操作...'%(DateTimeTool.getNowTime(),file_path))
        else: # 直接删除
                stdin, stdout, stderr, exit_code=sshClient.ssh_exec_command(delete_command)
                if exit_code==0:
                    print('%s 删除【%s】日志成功...'%(DateTimeTool.getNowTime(),file_path))
                else:
                    print('%s 删除【%s】日志失败...%s'%(DateTimeTool.getNowTime(),file_path,stderr.read()))