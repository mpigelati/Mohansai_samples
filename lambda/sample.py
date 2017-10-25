'''In Python, anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.

Lambda Functions

Syntax of Lambda Function

lambda arguments: expression

Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.




'''

# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))

'''In the above program, lambda x: x * 2 is the lambda function. Here x is the argument and x * 2 is the expression that gets evaluated and returned.

This function has no name. It returns a function object which is assigned to the identifier double. We can now call it as a normal function. The statement'''

double = lambda x: x * 2

#is nearly the same as

def double(x):
   return x * 2

'''Use of Lambda Function

We use lambda functions when we require a nameless function for a short period of time.

In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
 Lambda functions are used along with built-in functions like filter(), map() etc.'''

# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)



my_list1=[2,4,6,7,8,9,10,20]

#new_my_list1=list(filter(lambda x:(x*2),my_list1))
new_list1   =list(filter(lambda x:(x*2) , my_list))

print(new_list1)

'''
def mul(val):

    return val*2

print("\n\n")
for i in my_list1:
    print(mul(i))'''







