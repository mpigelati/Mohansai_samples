# This file is to print command line arguments
import sys

print("hellow world")


list=[]

#list.append("hellow")
list.append(sys.argv[0])
list.append(sys.argv[1])
list.append(sys.argv[2])
list.append(sys.argv[3])

print(list)
print(len(list))

#length =len(list)
#print("length",length)
for file in range(0,len(list)):
    print("filename",list[file])

