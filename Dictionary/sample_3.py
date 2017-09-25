dict={'name':'mohan','age':30}

print(dict['name'])
print(dict['age'])
print(dict['sex'])


#error:- If we attempt to access a data item with a key, which is not part of the dictionary, we get an error as follows −
'''

Traceback (most recent call last):
  File "/home/mohansai/python/Mohansai_samples/Dictionary/sample_3.py", line 5, in <module>
    print(dict['sex'])
KeyError: 'sex'



'''