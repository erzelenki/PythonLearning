from math import sqrt
while True:
    try:
        a=int(input("ah "))
        print(1/sqrt(a))
    except ZeroDivisionError:
        print("na nol ne deli durilka")
    except ValueError:
        print("I 4to ty vvodish?")
