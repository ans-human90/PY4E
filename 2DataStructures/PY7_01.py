fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:",fname)
    quit()
for line in fhand:
    lnew=line.rstrip()
    print(lnew.upper())
