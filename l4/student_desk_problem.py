import math
class1=int(input("num os student in class1: "))
class2=int(input("num of student in class2: "))
class3=int(input("num of student in class3: "))
desk1=(class1)/2
desk2=(class2)/2
desk3=(class3)/2
t_num_desk=math.ceil(desk1+desk2+desk3)
#we r using ceil method in math module
print(t_num_desk)