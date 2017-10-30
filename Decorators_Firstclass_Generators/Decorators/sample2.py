def percent(func):
    print("6")
    def inner(*args, **kwargs):
        print("7")
        print("%" * 10)
        print("8")
        func(*args, **kwargs)
        print("%" * 20)
        print("9")
    return inner

#@star
@percent

def printer(msg):
    print(msg)

printer("Hello")