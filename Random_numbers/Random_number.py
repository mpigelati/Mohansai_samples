from random import *
'''#import random
#help(random)
#print(random())
#print(random(0,100))
#print (randint(1, 100))
#print(uniform(1,100))


#list=[1,2,3,4,5,6,7,8,9,10,11,12]

#shuffle(list)

#print(list)

#To pick a random number from a list:

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



x = sample(items, 10)  # Pick a random item from the list
print (x[0])

y = sample(items, 6)  # Pick 4 random items from the list
print (y)

items[3] =20
print(items)
#items1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#items1[5] =20
#print(items)
'''
"""
1:- 
items = [1, 2.13, 3.24, 4.25, 5.46, 6.57, 7.68, 8.79, 9.810, 10.911]
seq = [1, 2, 3, 4, 5]

# Get a list of 1 random numbers, convert to one random number.
randomElement = sample(items, 1)
print(randomElement)
print(randomElement[0])
randomElement = randomElement[0]
print(randomElement)

# Multiple every element of the list
for element in seq:
    y = element * randomElement
    print("y=", y)
"""

seq = [1, 2, 3, 4, 5]

# Get a list of 1 random numbers, convert to one random number.
randomElement = sample(seq, 1)
print(randomElement)
print(sample(seq, 1))
randomElement = randomElement[0]

# Multiple every element of the list, using list comprehension
l = [randomElement * x for x in seq]
print(l)

# Multiple every element using map
l = list(map(lambda x: randomElement * x, seq))
print(l)