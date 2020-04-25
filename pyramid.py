blocks = int(input("Enter the number of blocks: "))
height = 0
while blocks-height > 0:
    height+=1
    blocks-=height
    print(" "*int((134-height*2)/2),"**"*height," "*int((134-height*2)/2), sep="")

#
# Write your code here.
#	

print("The height of the pyramid:", height)
