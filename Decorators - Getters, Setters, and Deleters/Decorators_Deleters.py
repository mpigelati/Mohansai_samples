#https://www.youtube.com/watch?v=jCzT9XFZ5bw&index=6&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

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
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        self.first=None
        self.last=None

emp1=Employee("mohansai","pigelati")
print(emp1.__dict__)
emp1.first="manju"

print(emp1.fullname)
print(emp1.email)

emp1.fullname=("lekshana pigelati")
print(emp1.fullname)

print(emp1.first)
print(emp1.last)
del emp1.fullname