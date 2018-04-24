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
                line = line.split('||')
                ip = line[0]
                username = line[1]
                passwd = line[2]
                dir = line[3]
                regexs = line[4]
                howmanydays = line[5]
                isRemove = line[6]
                self._sshclient = SSHClient(ip, username, passwd)
                execute_command = "cd /hskj/scripts && python deleteLogs.py "+dir+' '+regexs+' '+howmanydays+' '+isRemove
                stdin, stdout, stderr, exit_code = self._sshclient.ssh_exec_command("mkdir -p /hskj/scripts")
                if exit_code:
                    print "Mkdir Fail!"+'\r\n'+stderr.read()
                    continue
                self._sshclient.sftp_put('deleteLogs.py', os.path.join('/hskj/scripts', "deleteLogs.py"))
                stdin, stdout, stderr, exit_code=self._sshclient.ssh_exec_command(execute_command)
                if exit_code:
                    print "Execute Fail!"+'\r\n'+stderr.read()
                    continue
                delscript_command = "cd /hskj/scripts && rm -rf deleteLogs.py"
                stdin, stdout, stderr, exit_code = self._sshclient.ssh_exec_command(delscript_command)
                if exit_code:
                    print "Delete Scripts Fail!" + '\n' + stderr.read()
                self._sshclient.closeSSHAndSFTP()

if __name__=='__main__':
    delLogs = RemoteDelLogs()
    delLogs.runRemoteDelLogs()
