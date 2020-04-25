from random import random
secret = int(random()*100)

new = int(input("new "))
while secret != new:
    if secret < new:
        print(" - ")
    else:
        print(" + ")
    new = int(input("new "))
print(new, "=", secret)
