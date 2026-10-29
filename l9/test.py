#finding mid element in str
# str="1234567890"
# len_str=len(str)
# mid_str=int(len_str/2)
# print(str[mid_str])
# str=input("enter someting: ")
# if len(str)%2!=0:
#     mid_str=int((len(str)/2))
#     print(str[mid_str])
# else:
#     len(str)%2==0
#     mid_str=int((len(str))/2)
#     print(str[mid_str-1],str[mid_str])
# num=int(input("enter a num: "))
# if num%2==0:
#     print("even")
# else:
#     print("odd")
dat=int(input("enter date: "))
mon=int(input("enter month: "))
yer=int(input("enter year: "))
if mon<1 or mon>12 or dat<1 :
    print("invalid")
elif mon in[1,3,5,7,8,10,12] and 32>dat>0:
    print("valid")
elif mon in[4,6,9,11] and 31>dat>0:
    print("valid")
elif mon in[2] and yer%4!=0 and 0>dat>29:
    print("vaild")
elif mon in[2] and (yer%400==0 or (yer%4==0 and yer%100!=0)) and (0>dat>30):
    print("valid")  