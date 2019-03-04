#-*- coding:utf8 -*-
import os
from sshClient import SSHClient

class RemoteDelLogs():
    def __init__(self):
        pass
    def runRemoteDelLogs(self):
        '''
        :return:
        '''
        with open('Info','r') as f:
            for line in f.readlines():
                if '#' not in line:
                    line=line.replace('\n','')
                    line = line.split('||')
                    ip = line[0]
                    username = line[1]
                    passwd = line[2]
                    dir = line[3]
                    regexs = line[4]
                    howmanydays = line[5]
                    isRemoveFile = line[6]
                    isRemoveDirs = line[7]
                    self._sshclient = SSHClient(ip, username, passwd)
                    execute_command = "cd /hskj/scripts && python deleteLogs.py "+dir+' '+regexs+' '+howmanydays+' '+isRemoveFile+' '+isRemoveDirs
                    stdin, stdout, stderr, exit_code = self._sshclient.ssh_exec_command("mkdir -p /hskj/scripts")
                    if exit_code:
                        print "mkdir /hskj/scripts fail!"+'\r\n'+stderr.read()
                    self._sshclient.sftp_put('deleteLogs.py', os.path.join('/hskj/scripts', "deleteLogs.py"))
                    stdin, stdout, stderr, exit_code=self._sshclient.ssh_exec_command(execute_command)
                    if exit_code:
                        print "execute python deleteLogs.py fail!"+'\r\n'+stderr.read()
                    delscript_command = "cd /hskj/scripts && rm -rf deleteLogs.py"
                    stdin, stdout, stderr, exit_code = self._sshclient.ssh_exec_command(delscript_command)
                    if exit_code:
                        print "delete deleteLogs.py fail!" + '\n' + stderr.read()
                    self._sshclient.closeSSHAndSFTP()

if __name__=='__main__':
    delLogs = RemoteDelLogs()
    delLogs.runRemoteDelLogs()
