x1=int(input("enter 1st vertex x coordinate: "))
y1=int(input("enter 1st vertex y coordinate: "))
x2=int(input("enter 2st vertex x coordinate: "))
y2=int(input("enter 2st vertex y coordinate: "))
x3=int(input("enter 3st vertex x coordinate: "))
y3=int(input("enter 3st vertex y coordinate: "))

# ab12 ac12 bc12
# ab13 ac13 bc13 
# ab23 ac23 bc23

if (x1==x2)and(y1==y2):
    print(x3,y3)
elif (x1==x2)and(y1==y3):
    print(x3,y2)
elif (x1==x2)and(y2==y3):
    print(x1,y1)
elif (x3==x1)and(y3==y2):
    print(x2,y1)
elif (x3==x1)and(y2==y1):
    print(x2,y3)
elif (x3==x1)and(y3==y1):
    print(x2,y2)
elif (x2==x3)and(y1==y2):
    print(x1,y3)
elif (x2==x3)and(y1==y3):
    print(x1,y2)
elif(x2==x3)and(y2==y3):
    print(x1,y1)