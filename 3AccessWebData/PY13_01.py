import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xml = urllib.request.urlopen(url, context=ctx).read()

print('Retrieved',len(xml),'characters')

tree = ET.fromstring(xml.decode())
lst = tree.findall('.//count')
print('Count:', len(lst))

newlist=list()
for item in lst:
    tmp=int(item.text)
    newlist.append(tmp)

#print('Newlist:',newlist)
print('Sum:',sum(newlist))
