'''Python has an interesting feature called decorators to add functionality to an existing code.
This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.


def first(string):
    print(string)

second= first
second("hellow")
'''
"""
When you run the code, both functions first and second gives same output. Here, the names first and second refer to the same function object.

Functions can be passed as arguments to another function.



#def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc,10))
Furthermore, a function can return another function."""

"""def is_call():

    def is_returned():
        print("hellow babe")
    return is_returned()

is_call()"""

#Getting back To decorators


#def make_pretty(func): #is a decorator

#    def inner():
 #       print("I got decorated")
 #       func()
 #   return inner

#@make_pretty
#def ordinary():
#    print("I am ordinary")

#ordinary()

#pretty = make_pretty(ordinary)

#pretty()

#ordinary = make_pretty(ordinary)
#ordinary()

"""In the example shown above, make_pretty() is a decorator. In the assignment step.

pretty = make_pretty(ordinary)

The function ordinary() got decorated and the returned function was given the name pretty.
We can see that the decorator function added some new functionality to the original function. This is similar to packing a gift.
The decorator acts as a wrapper. The nature of the object that got decorated (actual gift inside) does not alter. But now, it looks pretty (since it got decorated).

Generally, we decorate a function and reassign it as,

ordinary = make_pretty(ordinary).

This is a common construct and for this reason, Python has a syntax to simplify this.
We can use the @ symbol along with the name of the decorator function and place it above the definition of the function to be decorated. For example,
"""

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

divide(2,5)
























