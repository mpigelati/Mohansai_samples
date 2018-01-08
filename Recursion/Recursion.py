#Limitations of recursions

"""
Everytime a function calls itself and stores some memory.
Thus, a recursive function could hold much more memory than a traditional function.
Python stops the function calls after a depth of 1000 calls. If you run this example:
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print (factorial(998))
#print (factorial(999)) # ERROR

"""
In other programming languages, your program could simply crash. You can resolve this by modifying the number of recursion calls such as:

"""
import sys

sys.setrecursionlimit(5000)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print (factorial(4998))
#print (factorial(4999))# ERROR
"""
but keep in mind there is still a limit to the input for the factorial function. For this reason, you should use recursion wisely.
As you learned now for the factorial problem, a recursive function is not the best solution.  For other problems such as traversing a directory, recursion may be a good solution.
"""