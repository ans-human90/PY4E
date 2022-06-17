fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)

count = 0
for line in fhand:
    if not line.startswith("From: ") :
        continue
    count=count+1
    nlist=line.split()
    print(nlist[1])

print("There were", count, "lines in the file with From as the first word")
