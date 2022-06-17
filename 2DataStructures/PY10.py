fname = input('Enter the file name: ')

if len(fname) < 1 :
     fname = "mbox-short.txt"

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dic=dict()
for line in fhand:
    nl=line.rstrip()
    words=nl.split()
    if len(words)<6 or words[0] != 'From' :
        continue
    time=words[5]
    nwrd=time.split(':')
    dic[nwrd[0]]=dic.get(nwrd[0],0) + 1

temp = list()
for k,v in dic.items() :
    newtup=(k,v)
    temp.append(newtup)
temp = sorted(temp)
for k,v in temp:
    print(k,v)
