import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = int(input("Enter count:"))
pos = int(input("Enter position:"))
names=list()

for i in range(count+1):
    print('Retrieving:',url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    lst=list()
    for tag in tags:
        ntg=str(tag.get('href', None))
        lst.append(ntg)
    name=re.findall('known_by_(.+).html',url)
    names.append(name)
    url=lst[pos-1]

print('Sequence of names:',names)
x=len(names)-1
print('The answer to the assignment for this execution is',names[x])
