class operations():

    def __add__(self, a,b):
        print("you are in add")
        return a+b

    def __sub__(self, a,b):
        print("you are in sub")
        return a-b

    def __mul__(self, a,b):
        print("you are in mul")
        return a*b


def main():
    print("hellow world")
    b=operations()
    print(b.__add__(10,20))


if __name__ == "__main__":
    main()