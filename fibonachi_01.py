
def fib(n):
    if n<0:
        return None
    if n==0 or n==1:
        return 1
    a0=1
    a1=1
    for i in range(n-1):
      a0,a1=a1,a0+a1
    return a1

#def fib(n):
#    if n<0:
#        return None
#    if n==0 or n==1:
#        return 1
#    return fib(n-1)+fib(n-2)
u=0
while u>=0:
    u=int(input("fibonachi "))
    print(fib(u))
