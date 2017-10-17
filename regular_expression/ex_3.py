import re
reg= r'([a-zA-Z]+) (\d+)'
str='June 24'

match = re.search(reg,str)
print(match)
if match:
    print("match at %s %s"%(match.start(),match.end()))
else:
    print("no match")

print("full match %s "%(match.group()))
print("full match group(%s) "%(match.group(0)))
print("full match gruop(%s) "%(match.group(1)))
print("full match gruop(%s) "%(match.group(2)))