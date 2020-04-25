def prostoje(x):
    for y in range (2,int(x/2+1)):
        if x%y == 0:
            return False
    return True

for a in range(1,999999):
    if a%10000 == 0:
        print (a)
    if not prostoje(a):
        continue
    for b in range (a,710000):
        if not prostoje(b):
            continue
        c=(a*a+b*b)**(1/2)
        if c==int(c):
            print(a,"\t",b,"\t",int(c))


