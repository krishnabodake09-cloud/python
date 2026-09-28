name=input("enter user name: ")
std=input("enter user std: ")
div=input("rnter user div: ")
sub1=int(input("enter maths score out of 100: "))
sub2=int(input("enter science score out of 100: "))
sub3=int(input("enter english score out of 100: "))
sub4=int(input("enter histroy score out of 100: "))
sub5=int(input("enter geography score out of 100: "))
t=sub1+sub2+sub3+sub4+sub5
p=t/5
print(f"{name} from {std}{div} got total of {t} out of 500, that is {p}%")
