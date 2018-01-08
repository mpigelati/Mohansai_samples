"""
Variables can only reach the area in which they are defined, which is called scope. Think of it as the area of code where variables can be used. Python supports
 global variables (usable in the entire program) and local variables.

By default, all variables declared in a function are local variables. To access a global variable inside a function, it’s required to explicitly define ‘global variable’.

"""


#Below we’ll examine the use of local variables and scope. This will not work:

def f(x, y):
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x * y))
    z = 4  # cannot reach z, so THIS WON'T WORK


z = 3
f(3, 2)

# but this will:

def f(x, y):
    z = 3
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x * y))
    print(z)  # can reach because variable z is defined in the function

f(3, 2)

#Calling functions in functions

#We can also get the contents of a variable from another function:
def highFive():
    return 5


def f(x, y):
    z = highFive()  # we get the variable contents from highFive()
    return x + y + z  # returns x+y+z. z is reachable becaue it is defined above


result = f(3, 2)
print(result)
"""
If a variable can be reached anywhere in the code is called a global variable. If a variable is known only inside the scope, we call it a local variable.
"""