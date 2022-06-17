from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

lst = list()
sum = 0

for tag in tags:
    strtag = str(tag)
    lst = re.findall('[0-9+]+',strtag)
    sum = sum + int(lst[0])
print(sum)
