def computepay(h,r):
    if h>40 :
        pay=(r*40)+(r*(h-40)*1.5)
    else:
        pay=h*r
    return pay

hrs=input("Enter Hours:")
fh=float(hrs)
rate=input("Enter Rate:")
fr=float(rate)
p=computepay(fh,fr)
print("Pay",p)
