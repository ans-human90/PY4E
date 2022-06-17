fname = input("Enter file name:")

if len(fname) < 1 :
    fname = "mbox-short.txt"

fhandle = open(fname)
dic=dict()
for line in fhandle:
    if not line.startswith("From: ") :
        continue
    nl=line.rstrip()
    w=nl.split()
    dic[w[1]]=dic.get(w[1],0) + 1
#print(dic)
bigcount= None
bigword= None
for k,v in dic.items() :
    if bigcount is None or v>bigcount :
        bigword=k
        bigcount=v

print(bigword,bigcount)
