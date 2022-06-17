import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

lst=list()
for tag in tags:
    ntg=str(tag)
    num=re.findall('[0-9]+',ntg)
    if len(num)<1:
        continue
    lst.append(num)

newlist=list()
for row in lst:
    for col in row:
        tmp=int(col)
        newlist.append(tmp)

print ('Count:',len(newlist))
print ('Sum:',sum(newlist))
