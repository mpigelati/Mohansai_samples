class Student:
    perc_rise=1.05
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age
        self.email=first+"."+last+"@gmail.com"

    def fullname(self):
        return "{}{}".format(self.first,self.last)

    def apply_raise(self):
        self.marks=int(self.marks * self.perc_rise)

class Dumb(Student): #inheritance
    def __init__(self, first, last, age,prog_lang):
        super().__init__(first,last,age)
        self.prog_lang = prog_lang

std_1 = Student("Mohansai","pigelati",30)
std_2 = Student("Saketh","settipalli",12)
print(std_1.last)
print(std_1.__dict__)
print(std_2.__dict__)

#print(std_1.age)
std_D_1 =Dumb("vachan","settipalli",9,"C")
print(std_D_1.__dict__)

#print(help(Dumb))

std_D_2 =Dumb("Deeraj","kuronthala",10,"python")
#print(std_D_2.prog_lang)
print(std_D_2.__dict__)