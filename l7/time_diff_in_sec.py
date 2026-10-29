h1=int(input("enter hours of 1st timestamp: "))
m1=int(input("enter minutes of 1st timestamp: "))
s1=int(input("enter secounds of 1st timestamp: "))

h2=int(input("enter hours of 2st timestamp: "))
m2=int(input("enter minutes of 2st timestamp: "))
s2=int(input("enter secounds of 2st timestamp: "))

time1=h1*3600+m1*60+s1
time2=h2*3600+m2*60+s2
diff=time1-time2
print("time difference in second: ",diff)