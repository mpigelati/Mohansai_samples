"""
Local variables

Local variables can only be reached in their scope.
The example below has two local variables: x and y.
"""

def sum(x, y):
    sum = x + y
    return sum


print(sum(8, 6))

"""

The variables x and y can only be used inside the function sum, they don’t exist outside of the function.
Local variables cannot be used outside of their scope, this line will not work:

"""