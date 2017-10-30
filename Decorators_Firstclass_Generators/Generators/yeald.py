'''
It is fairly simple to create a generator in Python.
It is as easy as defining a normal function with yield statement instead of a return statement.
If a function contains at least one yield statement (it may contain other yield or return statements),
it becomes a generator function. Both yield and return will return some value from a function.
The difference is that, while a return statement terminates a function entirely,
 yield statement pauses the function saving all its states and later continues from there on successive calls.'''

"""
def generatots(num):
    n=0
    while(n<num):
        yield n
        n=n+1

gen =generatots(10)
for i in gen:
    print(i) """

def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

counter = 0
for x in f:
    print (x),
    counter += 1
    if (counter > 10): break
print