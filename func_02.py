def isItATriangle(a, b, c):
    return a+b>c and a+c>b and c+b>a
tri=[1,2,2]
brk=True

while tri[0]>0 and tri[1]>0 and tri[2]>0:
    for i in range(3):
        print("input side #",i,"= ",end="")
        tri[i]=float(input())
        if tri[i]<=0:
            brk=False
            break
            
    if (not isItATriangle(tri[0],tri[1],tri[2])) and brk:
        print("Nikakoj")
        print()
        continue
    if brk:
        if tri[0]>tri[1] and tri[0]>tri[2]:
            c=0
            a=1
            b=2
        if tri[1]>tri[0] and tri[1]>tri[2]:
            c=1
            a=0
            b=2
        c=2
        a=1
        b=0
        if tri[c]**2 == tri[a]**2+tri[b]**2:
            print("priamougolnyj")
            print()
        else:
            print ("oby4nyj")
            print()
    else:
        print("Poka")



