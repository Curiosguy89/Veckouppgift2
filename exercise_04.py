#Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
#Version 1, exempel på output:

#Skriv in en temperatur i grader Celsius: 22
#Det blir 71.6 grader Fahrenheit.

#Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit.
# Sedan räknar programmet om till den andra temperaturen.
#Tips: be användaren skriva in t.ex. "F" om man vill ange temperaturen i i Fahrenheit. Använd sedan if + else.

#Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta på sig vinterkläder.
# Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.

#Version 1

temp_c = float (input (" Skriv en temperatur i Celcius: "))
temp_c_to_f = 1.8 * temp_c + 32
print( "Temperatur i Fahrenheit: ", temp_c_to_f)

#Version 2
temp_option = int(input (" Skriv 1 för att omvandla Celsius eller 2 för att omvandla Fahrenheit: "))
if temp_option == 1:
    unit = "Celsius"
else:
    unit = "Fahrenheit"
temperatur = float (input(f"Skriv en temperatur i {unit}: "))
if unit == "Celsius":
    temp_c_to_f = 1.8 * temp_c + 32
    temp_c_to_f = temperatur
    print( "Temperatur i Fahrenheit: ", temp_c_to_f)
if unit == "Fahrenheit":
    temp_f_to_c =  (temperatur - 32) / 1.8
    temp_f_to_c = temperatur
    print( "Temperatur i Celsius: ", temp_f_to_c)
if temp_f_to_c < 50 or temp_c_to_f < 10:
    print( "Klä på dig vinterkläder!")
elif temp_f_to_c >= 68.0 or temp_c_to_f >= 20.0:
    print( "Soligt och skönt! Ta på dig badkläder")





