

import paramiko

if __name__ == '__main__':
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='hostname', username='mokgadi', password='mypassword')

    stdin,stdout,stderr=ssh_client.exec_command("ls")
    print(stdout.readlines())
    print(stderr.readlines)

    #Downloading a file from remote machine
    ftp_client=ssh_client.open_sftp()
    ftp_client.get('remotefileth','localfilepath')
    ftp_client.close()
    #Uploading file from local to remote machine
    ftp_client=ssh_client.open_sftp()
    ftp_client.put('localfilepath','remotefilepath')
    ftp_client.close()











