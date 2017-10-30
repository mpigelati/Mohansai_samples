import  re

def all_matches(text,pattern):
    print(pattern)
    regobj = re.compile(pattern)
    for m in regobj.finditer(text):
        print(str(m.start()) + "-" + str(m.end()) + ":"+text[m.start():m.end()] )

text ="xyyxxxxxyyyyxxxxyy"
pattern1= "xy*"
pattern2= "xy+"
pattern3= "xy?"
pattern4= "xy{2}"
pattern5= "xy{2,4}"
pattern6= "xy{2,}"
pattern7= "xy*?"
pattern8= "xy+?"
pattern9= "xy?"
pattern10= "xy{2}?"
pattern11= "xy{2,}?"
pattern12= "xy{2,4}?"
pattern13= "x[xy]+"

#all_matches(text,pattern1)
#print("\n")
#all_matches(text,pattern2)
#print("\n")
#all_matches(text,pattern3)
#print("\n")
#all_matches(text,pattern4)
#print("\n")
#all_matches(text,pattern5)
#print("\n")
#all_matches(text,pattern6)
#print("\n")
#all_matches(text,pattern7)
#print("\n")
#all_matches(text,pattern8)
#print("\n")
#all_matches(text,pattern9)
#print("\n")
#all_matches(text,pattern10)
#print("\n")
#all_matches(text,pattern11)
#print("\n")
#all_matches(text,pattern12)
print("\n")
all_matches(text,pattern13)