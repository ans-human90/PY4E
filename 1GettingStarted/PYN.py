x=input('N=')
if int(x)>1 :
    print('its positive number')
print('done with if statement')
for i in range(5) :
    print('start with',i)
    if i>2 :
        print('wow bigger than 2')
    print('done with',i)
print('all done with 1st program')
y=input('any number n=')
if int(y)>1 :
    print('greater than one')
    if int(y)<100 :
        print('also less than 100')
    else :
        print('also greater than 100')
print('all done with 2nd program')
if int(y)%2==0 :
    print('even')
else :
    print('odd')
# taking value of n from the 1st part of this
if int(x)<5 :
    print('small')
elif int(x)<10 :
    print('medium')
else :
    print('large')
print('all done')
