'''Python has an interesting feature called decorators to add functionality to an existing code.

This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

#decorators dynamically alter the functionality of a function
This is ideal when you need to extend the functionality of functions that you don't want to modify.
 We can implement the decorator pattern anywhere, but Python facilitates the implementation by providing much more
  expressive features and syntax for that.

'''

import time

def calc_square(numbers):
    result=[]
    for num in numbers :
        result.append(num*num)
    print("square",result)
    return result

def calc_cube(numbers):
    result=[]
    for num in numbers :
        result.append(num*num*num)
    print("cub",result)
    return result

array = range(1,10)
out_suare=calc_square(array)
#print(out_suare)
out_cube=calc_cube(array)
#print(out_cube)