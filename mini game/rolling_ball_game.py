import random
n=int(input("enter num of pins(N): "))
k=1
I='I'
N=list(I*n)
chance=1
go=""
while not chance==go:
    print(chance,"ball")
    for i in range(k):
        l=(random.randint(1,n))
        r=(random.randint(l,n))
        for j in range(l-1,r):
            N[j]='.'
    print(''.join(N))
    go=input()
    chance+=1
    #win conditions
    win_n=list('.'*n)
    if N==win_n:
        print(f"winner!!!\n you got the strick after {chance-1} chance")
        break