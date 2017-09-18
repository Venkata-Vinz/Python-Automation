# This code SSH into all the com servers and get the ifconfig and system info
#  from all the switches connected in each and every port (150 switches -> 3 com servers (approx 50 each)).

# Features: 1) SSH into devices
#           2) Interactively communicate with shells 
#           3) Interactively exits out of shell if that shell doesn't have the prompt which it needed.
# Disadvantage: 1) Password in clear text
#               

import paramiko
import time
import socket

def run_cmd():
	try:
		buff = ''
		while not buff.endswith('# '):
			resp = channel.recv(9999)xaz
			buff += resp
#		print buff			
		channel.send('ssh <username>@'+`i`+' -p '+`j` + '\n')
		buff = ''
		while not buff.endswith('Password: '):
			resp = channel.recv(9999)
			buff += resp
#		print buff

		channel.send('<enter your ssh password>' + '\n')
#		print 'password entered to login'
		channel.send('\n')
		channel.send('\n')
		channel.send('\n')
#		print 'entered next line'

		buff = ''
		while not buff.endswith('~# '):
			resp = channel.recv(9999)
			buff += resp
#		print buff
	
		channel.send('ifconfig ma1' + '\n')
			
		buff = ''
		while not buff.endswith('~# '):
			resp = channel.recv(9999)
			buff += resp
#		print buff
	
		channel.send('onie-shell' + '\n')
		
		buff = ''
		while not buff.endswith('/ # '):
			resp = channel.recv(9999)
			buff += resp
#		print buff
			
		channel.send('onie-sysinfo' + '\n')
		
		buff = ''
		while not buff.endswith('/ # '):
			resp = channel.recv(9999)
			buff += resp
		print buff
		
		ssh.close()

	except Exception as e:
		print "Socket timetout: " + str(e)
		print '\n'
		ssh.close()
		return

ip=['x.x.x.x', 'x.x.x.x', 'x.x.x.x'] # com servers ip addresses
ports = range(xx01, xx49)  # com servers ports range
for i in ip:
#	print i
	for j in ports:
		print ('-'*50)
		print `i`+ '    Port:'+`j`		
#		print j
		ip=i
		user='<user name>'
		password='<password>'
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(i, username=user, password=password)
		channel = ssh.invoke_shell()
		channel.settimeout(15)
		run_cmd()

print 'This is the end'
