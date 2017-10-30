import requests

http_page= 'https://www.tutorialspoint.com/python/python_loops.htm'

r = requests.get(http_page)

for line in r:
    print(line.strip())

print(r.headers)


