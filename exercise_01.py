
# Veckouppgift 1, Pris och rabatt
discount = 0
bli_medlem = input("Skriv ja om du vill bli medlem och ta del av våra rabatter:")
if bli_medlem == "ja":
    print("Grattis du är medlem nu!")
else:
    print("Du är inte medlem")

price = float(input ("Välkommen, hur mycket vill du handla för?"))
#pris endast för medlemmar

if bli_medlem == "ja":
    if 100 <= price < 300:
        print(f"Grattis! Du får 10% rabatt.")
        discount = 10

    elif price <= 300:
        print(f"Grattis! Du får 25% rabatt.")
        discount = 25
final_price = price * (100 - discount) / 100
print("Slutpris efter avdragen rabatt:", final_price)