### using for loop-----------------------------------------------------------------------------
# a=int("0123")
# for i in range(1,4):
#     pin=int(input("enter ur pin: "))
#     if pin==a:
#         print("valid pin")
#         balance=int(5000)
#         withdraw=int()
#         deposit=int()
#         if pin==a:
#             b=input("chose-\n     1)balance\n     2)withdraw\n     3)deposit\n     4)exit \n   enter: ")
#             if b=="balance":
#                 print(balance)
#             elif b=="withdraw":
#                 withdraw=int(input("enter withdraw amount: "))
#                 if withdraw<balance:
#                     print("remaining balance: ", balance-withdraw)
#                 else:
#                     print("insufficent balance")
#             elif b=="deposit":
#                 deposit=int(input("enter deposited amount :"))
#                 print(" current balance: ", balance+deposit)
#             else:
#                 print("exit")
#             print("thank you for using!!")
#             break        
# else:
#     print("ur acc has been block")
### using while loop-----------------------------------------------------------------------------
trial=3
while trial>0:
    a=int("0123")
    pin=int(input("enter ur pin: "))
    if trial==3:
        print("2 try remaining")
    if trial==2:
        print("1 try remaining")
    if pin==a:
        print("valid pin")
        balance=int(5000)
        withdraw=int()
        deposit=int()
        if pin==a:
            b=input("chose-\n     1)balance\n     2)withdraw\n     3)deposit\n     4)exit \n   enter: ")
            if b=="balance":
                print(balance)
            elif b=="withdraw":
                withdraw=int(input("enter withdraw amount: "))
                if withdraw<balance:
                    print("remaining balance: ", balance-withdraw)
                else:
                    print("insufficent balance")
            elif b=="deposit":
                deposit=int(input("enter deposited amount :"))
                print(" current balance: ", balance+deposit)
            else:
                print("exit")
            print("thank you for using!!")
            break
    trial-=1
else:
    print("ur acc has been block")