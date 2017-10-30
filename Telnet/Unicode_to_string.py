#you can use encode to ASCII if you don't need to translate the non-ASCII characters:

>>> a=u"aaaàçççñññ"
>>> type(a)
<type 'unicode'>
>>> a.encode('ascii','ignore')
'aaa'
>>> a.encode('ascii','replace')
'aaa???????'
>>>