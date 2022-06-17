import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved',len(data),'characters')

info = json.loads(data.decode())

info=info['comments']

lst=list()
for item in info:
    tmp=int(item['count'])
    lst.append(tmp)

print('Count:',len(lst))
print('Sum:',sum(lst))
