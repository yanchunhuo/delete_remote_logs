#-*- coding:utf8 -*-
import os
import re
import subprocess
import time
import sys
import shutil

class DeleteLogs():
    def __init__(self):
        pass
    def delete_logs(self, dirs, regexs, howmanydays, isRemoveFile,isRemoveDirs):
        '''
        :param dirs:扫描的目录
        :param regexs: 正则匹配的日志，以数组存放多个正则表达式
        :param howmanydays:删除几天前的日志
        :param isRemoveFile:是否删除文件，不删除则进行清空，1代表删除，0代表是清空
        :param isRemoveDirs:是否删除目录内的内容，若设置删除，则regexs、isRemoveFile参数均无效。1代表删除
        :return:
        '''
        if isRemoveDirs==1:
            for path, dirs, files in os.walk(dirs):
                for file in files:
                    filePath = os.path.join(path, file)
                    mtime = os.path.getmtime(filePath)
                    nowtime = time.time()
                    interval = (nowtime - mtime) / 3600 / 24
                    if interval > howmanydays:
                        os.remove(filePath)
                for dir in dirs:
                    dirPath =  os.path.join(path,dir)
                    mtime = os.path.getmtime(dirs)
                    nowtime = time.time()
                    interval = (nowtime - mtime) / 3600 / 24
                    if interval > howmanydays:
                        shutil.rmtree(dirPath)
                # 只对当前目录下的目录、文件进行删除
                break
        else:
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
                            if isRemoveFile==1:
                                os.remove(filePath)
                            else:
                                subprocess.check_output('>' + filePath, shell=True)

if __name__=='__main__':
    deleteLog = DeleteLogs()
    deleteLog.delete_logs(sys.argv[1],sys.argv[2].split(','),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))


