import re

fname = input('Enter the file name: ')

#default file sample
if len(fname) < 1 :
     fname = "regex_sum_42.txt"

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

lst=list()
for line in fhand:
    num=re.findall('[0-9]+',line)
    if len(num)<1:
        continue
    for n in num:
        tmp=int(n)
        lst.append(tmp)

print ('Final sum:',sum(lst))
