import telnetlib
import json
<<<<<<< HEAD:Assain/Telnet/my_files/_Temp_Telnet_project.py
import thread
=======
import unicodedata

>>>>>>> a0966198486e6b5013ef1fccbc8a5adc7bd42aec:Assain/Telnet/my_files/Telnet_project.py
def Fun_Telnet(localhost,user,password):

    HOST = localhost.encode('ascii', 'ignore')
    user = user.encode('ascii', 'ignore')
    password = password.encode('ascii', 'ignore')

    print(user)
    tn = telnetlib.Telnet(HOST)

    tn.read_until("login: ")
    tn.write(user + "\n")

    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("ls -la\n")
    tn.write("exit\n")

    print (tn.read_all())



json_file = "data.json"
json_data = open(json_file)
data = json.load(json_data)

for i in range(0,len(data)):
    Fun_Telnet(data[i]["Host"],data[i]["user"],data[i]["password"])
