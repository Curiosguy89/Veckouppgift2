
# Veckouppgift 1, Pris och rabatt
discount = 0
bli_medlem = input("Skriv ja om du vill bli medlem och ta del av våra rabatter:")
if bli_medlem == "ja":
    print("Grattis du är medlem nu!")
else:
    print("Du är inte medlem")

price = float(input ("Välkommen, hur mycket vill du handla för?"))
#pris endast för medlemmar
level1 = 100
level2 = 300
if bli_medlem == "ja":
    if level1 <= price < level2:
        print("Grattis! Du har uppnåt nivå 1 Du får 10% rabatt.")
        discount = 10
    elif price >= level2:
        print("Grattis! Du har uppnåt nivå 2 Du får 25% rabatt.")
        discount = 25
final_price = price * (100 - discount) / 100
print("Slutpris efter avdragen rabatt:", final_price)