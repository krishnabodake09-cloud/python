a=int(input("enter a number: "))
b=int(input("enter another number: "))
if a>b:
    max=a
elif a<b:
    max=b
else: max=a=b
print(f"the greatest num is {max}")
# for built in function
# m=max(a,b)