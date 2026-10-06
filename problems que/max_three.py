n1=int(input("enter 1st num: "))
n2=int(input("enter 2nd num: "))
n3=int(input("enter 3rd num: "))
if n1>=n2 and n1>=n3:
    print( n1 ,"num is greatest")
elif n2>=n1 and n2>=n3:
    print( n2 ,"num is greatest")
else:
    print( n3 ,"num is greatest")