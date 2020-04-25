def isPrime(num):
    for i in range(2,num//2+1):
       if num%i == 0:
           return False
    return True



primes=[]
for i in range(1, 104730):
	if isPrime(i + 1):
	    primes.append(i+1)

print("***********************************************************************************************")
print()
print (len(primes))
print()
print("***********************************************************************************************")
print(primes[-1])
