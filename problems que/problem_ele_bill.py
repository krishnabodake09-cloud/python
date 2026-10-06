unit=int(input("enter units: "))
rate=int(input("enter rate: "))
bill=unit*rate
blocks=unit//100
remaining=unit%100
print(f"bill={bill}, 100 unit block={blocks}, remainng={remaining}")