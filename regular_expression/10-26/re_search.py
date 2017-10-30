import re

print(re.search("pattern","searching patten in test"))# it is not matching
print(re.search("pattern","searching pattern in test"))#it is matching

match = re.search("pattern","searching pattern in test")#it is matching
print(match)

print(match.re.pattern)
print(match.string)
print(match.start())
print(match.end())
print(match.d)