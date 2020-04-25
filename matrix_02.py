ctoto = [[i**(1/(j+1)) for i in range (5)] for j in range (30)]
print (ctoto)
for i in range (30):
    print()
    for j in range (5):
        print (ctoto [i] [j], end="\t\t")
        
