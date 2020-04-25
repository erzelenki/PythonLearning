def readint(prompt, min_, max_):
    while True:
        try:
            value=int(input(prompt))
            if value in range (min_,max_+1):
                return value
            print ("Error: the value is not within permitted range (",min_,"..",max_,")",sep='')
        except ValueError:
            print ("Error: wrong input")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
