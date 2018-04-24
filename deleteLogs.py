#-*- coding:utf8 -*-
import os
import re
import subprocess
import time
import sys

class DeleteLogs():
    def __init__(self):
        pass
    def delete_logs(self, dirs, regexs, howmanydays, isRemove):
        '''
        :param dirs:扫描的目录
        :param regexs: 正则匹配的日志，以数组存放多个正则表达式
        :param howmanydays:删除几天前的日志
        :param isRemove:是否删除文件，不删除则进行清空
        :return:
        '''
        pattern = '|'.join(regexs)
        for path, dirs, files in os.walk(dirs):
            for file in files:
                filePath = os.path.join(path, file)
                if re.match(pattern, file):
                    # 获得文件最后修改时间
                    mtime = os.path.getmtime(filePath)
                    nowtime = time.time()
                    interval = (nowtime - mtime) / 3600 / 24
                    if interval > howmanydays:
                        if isRemove==0:
                            print filePath
                            os.remove(filePath)
                        else:
                            print '>' + filePath
                            subprocess.check_output('>' + filePath, shell=True)

if __name__=='__main__':
    deleteLog = DeleteLogs()
    deleteLog.delete_logs(sys.argv[1],sys.argv[2].split(','),int(sys.argv[3]),int(sys.argv[4]))


