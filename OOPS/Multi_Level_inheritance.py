class Gand_father:
    def S_Gfather(self):
        print("Grand father_1")
class Father(Gand_father):
    def S_father(self):
        print("father_2")
class Child(Father):
    def S_child(self):
        print("child_3")

d=Child()
d.S_child()
d.S_father()
d.S_Gfather()
