fname = input("Enter file name: ")
try:
    fhand = open(fname)

except:
    print("File cannot be opened:",fname)
    quit()

count=0
add=0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count=count+1
    ipos=line.find(':')
    piece=line[ipos+1:]
    value=float(piece)
    add=add+value

print("Average spam confidence:",add/count)
