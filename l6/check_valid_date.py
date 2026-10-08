d=int(input("enter day: "))
m=int(input("enter month: "))
y=int(input("enter year: "))
if m <1 or m>12:
    print("valid")
elif d<1 and 1>31:
    print("valid")
elif m in[4, 6,9,11] and d:
    print