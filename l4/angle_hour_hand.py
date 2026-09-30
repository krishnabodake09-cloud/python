
h=int(input("enter hour (0to12): "))
m=int(input("enter min (0to60): "))
s=int(input("enter sec (0to60): "))
a=(h*30)+(m*0.5)+(s*0.0083333)
ang=(a)
if ang>360:
    print(ang-360)
else:
    print(ang,"degree")