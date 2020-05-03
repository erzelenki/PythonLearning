#!\usr\bin\python3


summ = 0
for i in range(100000000):
    a=10-(10**0.0000000000000001)**(10000000000000000)
    summ = summ + a
print(summ)
