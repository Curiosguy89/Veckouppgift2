is_member = False
level1 = 100
level2 = 300
discount = 0

price = input ("Välkommen, köp något dyrt")
price = float(price)
if price > level1:
    print(f"Grattis! Du har avamncerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
if price >= level2:
    print(f"Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset...." + str(final_price))