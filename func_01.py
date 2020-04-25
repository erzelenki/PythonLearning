def isYearLeap(year):
    if year%4!=0:
        return False
    if year%100!=0:
        return True
    else:
        if year%400==0:
            return True
    return False

def daysInMonth(year, month):
    if (year<1654) or (month>12) or (month<1):
        return None
    if month == 2:
        if isYearLeap(year):
            return 29
        return 28
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    return 30


def dayOfYear(year, month, day):
    data=0
    if (year<1654) or (month>12) or (month<1) or (day<1):
        return None
    if daysInMonth(year,month)<day:
        return None
    for counter in range(month-1):
        counter+=1
        data+=daysInMonth(year,counter)
    return data+day
        
  

print(dayOfYear(2001, 2, 28))
