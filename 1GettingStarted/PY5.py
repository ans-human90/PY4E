largest = None
smallest = None
while True:
    snum = input("Enter a number: ")
    if snum == "done" :
        break
    try:
        fnum=float(snum)
        if smallest is None :
            smallest = fnum
        elif fnum < smallest :
            smallest = fnum
        if largest is None :
            largest = fnum
        elif fnum > largest :
            largest = fnum
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
