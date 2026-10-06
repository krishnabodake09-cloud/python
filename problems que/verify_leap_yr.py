y=int(input("enter year you want to check: "))
if y%4==0 and (y%100!=0 or y%400==0):
    print(y , 'is a leap year')
else:
    print(y , 'is not leap year')
#to accumodate extra 11min and 14sec 'y%100' is cosider