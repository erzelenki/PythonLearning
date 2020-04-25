from math import exp

x=1

try:
    while True:
        print(exp(x))
        x*=1.001
except OverflowError:
    print("Too big")
    
        
    

