class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@mail.com"

emp1=Employee("mohansai","pigelati")
print(emp1.__dict__)

emp1.first="manju"
print(emp1.__dict__) # here the draw back is the mail addredss is not updating