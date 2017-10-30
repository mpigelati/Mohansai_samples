import re

regex =re.compile('x(?P<first>[xy]+)(?P<secondary>)')

match= regex.search('xyxxxyxxxyxyxy')

print(match.groups())
