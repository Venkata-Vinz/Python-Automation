# This code takes IPs from file and pings every 5 minutes 
# and it will send an Email if the ping fails.
# Features: 1) password are hidden
#           2) SSH into remote system
#           3) Send the Email
#           4) Runs every 5 minutes
#           5) Takes IPs from file

import subprocess as s
import smtplib
import time
import re
import os
import getpass

#pass2 = raw_input ('Enter your Email id password: ')        # password in clear text
pass2 = getpass.getpass(prompt='Password: ', stream=None)    # To hide the password from clear text
#host = open("hosts.txt", "r")
host = open('hosts.txt').read().split("\n")
#ip=raw_input("Enter the IP/Domain name to ping:")
while True:
#	host = open('hosts.txt').read().split("\n")
	for i in host:
		response = os.system("ping "+i+" -n 1") ###(For Linux : response = os.system("ping -c 3 "+i+"")
		if response == 0:
			print i, 'is up!'
		else:
			print i, 'is down!'
#		if not(s.call(["ping",i])==0):
			output = 'check your IP: ' + i
			print output
			smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
			smtpObj.ehlo()
			smtpObj.starttls()
			smtpObj.login('<sending Email ID>', pass2)
			smtpObj.sendmail('<sending Email ID>', '<receiving Email ID>', 'Subject: PING RESPONSE\
			.\n ' + output)
			{}
			smtpObj.quit()
			time.sleep(100)