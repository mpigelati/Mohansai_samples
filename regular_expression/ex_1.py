import re

#str = 'an example word:cat!!'
str = 'an example word:cat!!'
#match = re.search(r'word:\w\w\w', str)
match = re.search(r'word:\w\w\w', str)
if match:
    print('found'.match.group())
else:
    print('did not find')