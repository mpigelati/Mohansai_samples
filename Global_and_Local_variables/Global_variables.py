"""
A global variable can be used anywhere in the code.
In the example below we define a global variable z

"""

z = 10

def afunction():
    global z
    print(z)

afunction()
print(z)

"""
The global variable z can be used all throughout the program, inside functions or outside.
A global variable can modified inside a function and change for the entire program:
"""

z = 10

def afunction():
    global z
    z = 9


afunction()
print(z)


#After calling afunction(), the global variable is changed for the entire program.
"""
Local and global variables can be used together in the same program.
Try to determine the output of this program:
"""

z = 10

def func1():
    global z
    z = 3


def func2(x, y):
    global z
    return x + y + z


func1()
total = func2(4, 5)
print(total)
