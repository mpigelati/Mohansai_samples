#As the name suggests, filter creates a list of elements for which a function returns true.

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)



n=[4,3,2,1]

data = list(filter(lambda x:x>2,n))

print ("data",data)


fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = (filter(lambda x: x % 2, fibonacci))
print(odd_numbers)