n=int(input("enter num of pins: "))
k=int(input("enter num of balls: "))
pins=["I"]*n
for i in range(k):
    start, end =map(int,input(
        f"enter range for ball {i+1:}: 1").split())
    for j in range (start-1,end):
        pins[j]="."

print("".join(pins))