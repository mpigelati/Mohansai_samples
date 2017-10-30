import re

def all_matches(text,pattern):
    print(pattern)
    regobj = re.compile(pattern)
    for m in regobj.finditer(text):
        print(str(m.start()) + "-" + str(m.end()) + ":"+text[m.start():m.end()] )


#all_matches("xx..  ..yyyxxx.. ", "[^. ]+")
#all_matches('A94B2c4 xyz08','[A-Z][0-9]')
#all_matches('A94B2c4 xyz08','[A-Za-z][0-9]')

#all_matches('silk road','s.+k')
#all_matches('Thsi is 1-st example',r'\d+')
#all_matches('Thsi is 1-st example',r'\D+')
#all_matches('Thsi is 1-st example',r'\D+')
#all_matches('This is 1-st example',r'\S+')
#all_matches('This is 1-st example',r'\s+')
#all_matches('This is 1-st example',r'\w+')
#all_matches('This is 1-st example',r'\W+')

