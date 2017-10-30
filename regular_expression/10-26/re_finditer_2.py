import re

def all_matches(text,pattern):
    print(pattern)
    regobj = re.compile(pattern)
    for m in regobj.finditer(text):
        print(str(m.start()) + "-" + str(m.end()) + ":"+text[m.start():m.end()] )


all_matches('Relative positionin  in regular expression ',r'^\w+')
all_matches('Relative positionin  in regular expression ',r'\A\w+')
#all_matches('Relative positionin  in regular expression ',r'\br|w+')
#all_matches('Relative positionin  in regular expression ',r'\Bg\B')
#all_matches('Relative positionin  in regular expression ',r'\bg\b')