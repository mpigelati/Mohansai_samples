class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)


emp1=Employee("mohansai","pigelati")
print(emp1.__dict__)

emp1.first="manju"
print(emp1.fullname)
print(emp1.email)