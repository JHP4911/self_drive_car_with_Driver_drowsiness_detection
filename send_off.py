import paramiko
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.43.166',username='pi',password='raspberry')
ftp = ssh_client.open_sftp()
file=ftp.file('saini.txt', "w", -1)
file.write('off')
file.flush()
ftp.close()
