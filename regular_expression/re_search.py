import  re

# ex:- 1
patterns = ['this','This','that']
text = 'Does this text match the pattern? this'

for pattern in patterns:
    print('looking for "%s" in %s'%(pattern,text) )

    if re.search(pattern,text):
        print ("fount match")
    else:
        print("not forund")


#ex:-2

pattern1 = " this "
text = 'Does this text match the pattern? this'

match=re.search(pattern1,text)

print(match)
s = match.start()
e = match.end()
print("start:- %s end:- %s"%(s,e))

#ex:-3




