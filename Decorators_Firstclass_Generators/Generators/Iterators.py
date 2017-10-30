'''
    Python iterator objects are required to support two methods while following the iterator protocol.
iter :- __iter__ returns the iterator object itself. This is used in for and in statements.

next :- __next__ method returns the next value from the iterator. If there is no more items to return then it should raise StopIteration exception

'''
'''
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next()

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
next(my_iter)'''

"""
Traceback (most recent call last):
  File "/home/mohansai/python/B_Python_work/Assain/Generators/Iterators.py", line 31, in <module>
    next(my_iter)
StopIteration"""

my_list = [4, 7, 0, 3]
iter_obj = iter(my_list)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break