
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['office']="innominds" # update record

print ("dict['Age']:", dict['Age'])
print ("dict['office']:", dict['office'])

del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

print ("dict['Age']:", dict['Age'])
print ("dict['office']:", dict['office'])