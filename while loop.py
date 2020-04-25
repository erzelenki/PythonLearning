from random import random
secret = int(random()*100)
n=1
new = int(input("new "))
while secret != new:
    if secret < new:
        print(" - ")
    else:
        print(" + ")
    new = int(input("new "))
    n += 1
print(new, "=", secret)
print("You Win in ", n, "steps")
