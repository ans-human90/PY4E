fname = input("Enter file name: ")
fhand = open(fname)
flist = list()
for line in fhand:
    nl=line.rstrip()
    nlt=nl.split()
    for i in nlt:
        if i not in flist:
            flist.append(i)

flist.sort()
print(flist)
