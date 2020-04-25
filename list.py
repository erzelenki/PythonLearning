mylist=[975,946,875,765,654,543,421,356,258,156,94,89,75,64,54,34,26,23,21,20,19,14,13,7,4,2,1,0]


print (mylist)

swapped=True
counter=0
while swapped:
    swapped=False
    counter+=1
    for i in range(len(mylist)-1):
        if mylist[i] > mylist[i+1]:
            mylist[i],mylist[i+1] = mylist[i+1],mylist[i]
            swapped=True
print (mylist)
print (len(mylist))
print (counter)




