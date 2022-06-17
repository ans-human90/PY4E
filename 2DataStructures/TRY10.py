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
    #print(time)
    newtime=time.split(':')
    dic[newtime[0]]=dic.get(newtime[0],0) + 1
#print(dic)
temp = list()
for k,v in dic.items() :
    newtup=(k,v)
    temp.append(newtup)
#print(temp)
temp = sorted(temp)
for k,v in temp:
    print(k,v)
