# Sportresultat

#Version 1 och 2 : Ett program som frågar användaren hur många mål respektive lag gjorde,
# och talar om vilket lag som vann eller om matchen blev oavgjord.

Tottenham_goals = int (input("hur många mål gjorde Tottenham?"))
Liverpool_goals = int (input("Hur många mål gjorde Liverpool?"))
if Tottenham_goals > Liverpool_goals:
    print("Tottenham vann!")
if Liverpool_goals > Tottenham_goals:
    print("Liverpool vann!")
if Tottenham_goals == Liverpool_goals:
    print("Båda lagen gjorde lika många mål och matchen blev oavgjort!")

#Version 3 nu ska programmet tala om hur många mål mer laget vann med. Exempel:
#Tottenham vann med 1 mål!

if Tottenham_goals > Liverpool_goals:
    skillnad = Tottenham_goals - Liverpool_goals
    print("Tottenham vann med",skillnad, "mål")
if Liverpool_goals > Tottenham_goals:
    skillnad = Liverpool_goals - Tottenham_goals
    print("Liverpool vann med",skillnad, "mål")
if  Liverpool_goals == Tottenham_goals:
    print("Tottenham gjorde", Tottenham_goals,"mål, och Liverpoool gjorde", Liverpool_goals, "mål, matchen blev oavgjort!")

# här kan man också skriva if på rad 18, elif på rad 21 och else på rad 24 ist'llet för massa if.