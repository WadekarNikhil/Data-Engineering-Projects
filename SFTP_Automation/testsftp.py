import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='192.168.138.10', username='user', password='123456', allow_agent=False, look_for_keys=False)

sftp = client.open_sftp()
sftp.put('test.txt.txt', 'uploaded.txt')
sftp.close()
