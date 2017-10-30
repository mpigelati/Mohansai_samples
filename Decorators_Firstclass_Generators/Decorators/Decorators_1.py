import time

def calc_square(numbers):
    start=time.time()
    result=[]
    for num in numbers :
        result.append(num*num)
    print("square",result)
    end=time.time()
    print(str((end-start*1000)))
    return result

def calc_cube(numbers):
    start=time.time()
    result=[]
    for num in numbers :
        result.append(num*num*num)
    print("cub",result)
    end=time.time()
    print(str((end - start * 1000)))
    return result

array = range(1,10)
out_suare=calc_square(array)
#print(out_suare)
out_cube=calc_cube(array)
#print(out_cube)