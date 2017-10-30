#https://www.python-course.eu/python3_lambda.php
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
#print product


from functools import reduce
product1 = reduce((lambda x, y: x * y), [1, 2, 3, 4])
#print product1




n=[5,4,3,2,1,]
print (reduce(lambda x,y:x*y,n))


data= reduce(lambda x,y:x+y,n)
print (data)
