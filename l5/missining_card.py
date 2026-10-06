n=int(input("enter the total number of cards: "))
remaing_num=sum(list(map(int,input("enter remaing cards: ").split())))
total_num_cards=n*(n+1)/2
print(total_num_cards-remaing_num)



