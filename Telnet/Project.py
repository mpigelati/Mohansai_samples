from telnetlib import Telnet
from sys import argv

def Fun_Telnet(Host,user,password):
    tn = Telnet(Host)
    print("telnet",tn)

    tn.read_until("login: ")
    tn.write(user +"\n")

    if password:
        tn.read_until("Password: ")
        tn.write(password +"\n")
        tn.write("ls -la \n")
        tn.write("exit\n")
        print (tn.read_all())


def Fun_Thread(data):
    print("this isthread function")
    print(data)



def Fun_linesplit(line):
    if ("Host" in line) | ("user" in line )|("password" in line):
        value = "".join(line.split(":")[0])
        keys = "".join(line.split(":")[1])
        temp = value.strip("\t").strip(' /"')
        temp1 = keys.strip("\t").strip(' /"').rstrip("\n").rstrip("\" ")
        return temp1

def Fun_to_open_file(filename,mode):
    try:
        fd= open(filename,mode)
    except:
        print("failed to open file")
    else:
        return fd


fd = Fun_to_open_file(argv[1],"r")
data = fd.readlines()
ldata=[]
count=0

count=len(data)
for i, line in enumerate(data):
    if ("Host" in line):
        ldata.append(Fun_linesplit(line))
        for j in (i+2,count):
            print("line ",j)
        print(" ")
        print("list",ldata)
        Fun_Thread(ldata)

