"""

The range() function returns of generates a sequence of numbers, starting from the lower bound to the upper bound.

range(lower_bound, upper_bound, step_size)
lower_bound: The starting value of the list.
upper_bound: The max value of the list, excluding this number.
step_bound: The step size, the difference between each number in the list.
->The lower_bound and step_size parameters are optional. By default the lower bound is set to zero, the incremental step is set to one. The parameters must be of the type integers, but may be negative.
"""

#range implementation difference
"""
This distinction won’t usually be an issue. The range() is implemented slightly different in the Python versions:

Python 2.x: The range() function returns a list.
Python 3.x: The range() function generates a sequence.

range in python 2.7
A call to range(5) will return: 0,1,2,3,4.

>>> range(5)

A call to range(1,10) returns: 1,2,3,4,5,6,7,8,9

>>> range(1,10)
Calling range(0,10,2) returns: 0,2,4,6,8

>>> range(0,10,2)
range in python 3
To generate a list using range, add the list function

>>> list(range(5))
We can use all parameters (lower bound, upper bound, step)

>>> list(range(0,10,2))
[0, 2, 4, 6, 8]
python 2 implementation
This version of range() allocates computer memory and also populates the computer memory behind the scenes. For large ranges, this is implementation is not very efficient.

Usually you won’t have any issues with the Python2 implementation of range() but if you use large numbers (millions of items) you could run into issues.
"""
