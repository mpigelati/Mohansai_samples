# Thiis is a simple android module for connecting remote PC
import telnetlib

HOST = "localhost"
user = "manju"
password = "jnjnuhuh"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")

if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls -la \n")

tn.write("exit\n")
print (tn.read_all())
