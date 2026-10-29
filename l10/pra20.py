n=int(input("enter a num: "))
if n>0:
    for i in range(0,n):
        i+=1
       # print(i)               # vertical print
        print(i , end="|")   # horizontal print
else:
    print(" please positive integer")