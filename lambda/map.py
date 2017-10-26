'''



The syntax of map() is:

map(function, iterable, ...)

map() Parameter

    function - map() passes each item of the iterable to this function.
    iterable iterable which is to be mapped

Return Value from map()

The map() function applies a given to function to each item of an iterable and returns a list of the results.

The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) and so on.

def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

Example 2: How to use lambda function with map()?


numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)


'''


list=[4,3,2,1]
def square(list1):
    list2=[]
    for num in list1:
        list2.append(num**2)
    return list2


print(square(list))



#ex:- 1
items = [1, 2, 3, 4, 5]
squared = (map(lambda x: x**2, items))

print squared



def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = (map(lambda x: x(i), funcs))
    print(value)