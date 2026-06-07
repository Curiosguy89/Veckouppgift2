# Veckouppgift 2, Balder

#Man måste vara 130cm lång för att åka Balder.Programmet ska säga om man får åka.


user_length = float(input( "vänligen ange din längd i cm:"))
if user_length >= 130:
    print("Din längd är tillåten!")
if user_length < 130:
    print("Din längd är inte tillåten, minimum längd är 130cm!")

