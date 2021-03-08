import getpass
import sys
import telnetlib

HOST = "192.168.246.94" 
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

telnet = telnetlib.Telnet(HOST)
telnet.read_until("sername: ",3)
telnet.write(user + "\n")
if password:
   telnet.read_until("assword:",3)
   telnet.write(password + "\n")

telnet.write("show ip int br\n")
telnet.write("configure terminal\n")
telnet.write("interface loopback 0\n")
telnet.write("ipv4 address 172.16.0.1/24\n")
telnet.write("exit\n")
telnet.write("commit\n")
telnet.write("exit\n")
telnet.write("show ip int br\n")
telnet.write("exit\n")

print telnet.read_all()