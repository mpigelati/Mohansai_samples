import csv

fd=open("sample1.csv","w")
dic = {"John": "john@example.com", "Mary": "mary@example.com",} #dictionary

colum_title="Firstname, Lastname\n"
fd.write(colum_title)

for key in dic.keys():
    name=key
    email=dic[key]
    row=name +','+email+"\n"
    fd.write(row)
fd.close()