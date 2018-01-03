class Father:
    def S_Father(self):
        print("Father_1")
class Mother:
    def S_Mother(self):
        print("Mother_2")
class Child(Father,Mother):
    def S_child(self):
        print("child_3")

d=Child()
d.S_Father()
d.S_Mother()
d.S_child()