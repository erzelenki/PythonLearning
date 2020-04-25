myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
i=0
while i < len(myList):
    if myList[i] in myList[i+1:]:
        del myList[i]
    else:
        i+=1
print("The list with unique elements only:")
print(myList)
