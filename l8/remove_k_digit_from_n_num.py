n=int(input("enter n: "))
k=int(input("enter k: "))
i=0
while i<k:
    n=n//10
    i+=1
if n==0:
    print("no digit remaining")
else:
    largest=0
    while n>0:
        digit=n%10
        if digit>largest:
            largest=digit
        n=n//10
print("largest digit: ",largest)
