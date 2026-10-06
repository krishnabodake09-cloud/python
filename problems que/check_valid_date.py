date=int(input("enter date(1to31): "))
month=int(input("enter month(1to12): "))
year=int(input("enter year(0to..): "))
if year%4==0 and (year%100!=0 or year%400==0):
    if month==2 and 1<=date<=29:
        print('valid date')
    elif month%2==0 and month!=2 and 1<=date<=30:
        print('valid date')
    elif month%2!=0 and 1<=date<=31:
            print('valid date')
elif year%4!=0:
    if month==2 and 1<=date<=28:
        print('valid date')
    elif month%2==0 and month!=2 and 1<=date<=30:
        print('valid date')
    elif month%2!=0 and 1<=date<=31:
        print('valid date')
else:
    print('invalid date')