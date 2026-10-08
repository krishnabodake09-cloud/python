a=float(input("enter 1st num: "))
b=float(input("enter 2nd num: "))
c=float(input("enter 3rd num: "))
if a>=b and a>=c:
    max=a
elif b>=a and b>=c:
    max=b
else:
    max=c
print("maximum number is: ",max)