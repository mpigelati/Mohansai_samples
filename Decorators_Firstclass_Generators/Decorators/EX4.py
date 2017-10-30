
from time import sleep


def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        #print(wrapper(*args, **kwargs))
        sleep(2)
        print("function",function(*args, **kwargs))
        return function(*args, **kwargs)

    #print("wrap",wrapper)
    return wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_number(num))
