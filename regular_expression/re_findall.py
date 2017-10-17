import  re

#str= "mohansai pigelati@gmail.com,saketh ram@gmail.com,vachan ram@gmail.com"
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
#emails = re.findall(r'[w.-]+@[w.-]+', str)
emails = re.findall(r'[w.-]+@[w.-]+', str)

print(emails)
for email in emails:
    print(email)



#ex:-2

text = 'abbaaabbbbaaaaa'
pattern2='ab'

for match in re.findall(pattern2,text):
    print('founf%s'%match)


print(match)


