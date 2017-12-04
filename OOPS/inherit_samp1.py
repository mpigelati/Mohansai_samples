class Student:
    per_rise=1.05
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first+"."+last+"@gmail.com"

    def fullname(self):
        return "{}{}".format(self.first,self.last)

    def apply_raise(self):
        self.marks=int(self.marks * self.per_rise)

class Dumb(Student): #inheritance
        pass

std_1 = Student("Mohansai","pigelati",30)
std_2 = Student("Saketh","settipalli",12)
print(std_1.last)
print(std_1.__dict__)
print(std_2.__dict__)


std_D_1 =Dumb("vachan","settipalli",9)
print(std_D_1.__dict__)

print(help(Dumb))
