import telnetlib
import json
import unicodedata
import thread
import os

def Fun_Telnet (localhost,user,password):
    print("you are in function Tenet")
    print(thread.get_ident())
    HOST = localhost.encode('ascii', 'ignore')
    user = user.encode('ascii', 'ignore')
    password = password.encode('ascii', 'ignore')

    #HOST ='localhost'
    #user ="moamsai"
    #password ="jnjnuhuh"

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
print(os.getpid())
for i in range(0,len(data)):

    try:
        thread.start_new_thread(Fun_Telnet, (data[i]["Host"],data[i]["user"],data[i]["password"]))
    except:
        print("failed to create thread")
    else:
        print("sucessfully started thread")

while 1:
    pass
