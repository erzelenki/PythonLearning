matrix=[x*y for x in range(10) for y in range(10)]
print(matrix)
for i in range(10):
    print()
    for j in range(10):
        print(matrix[j],[i], "\t",end='')
        
