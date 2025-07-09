# számológép **=hatványozás      %= maradékososztás     //=úgy oszt hogy lekerekít (nincs tizedes)
number1 = int(input("1.szám:\n"))
muvelet = input("Művelet:\n")
number2 =int(input("2. szám:\n"))
if muvelet == "+":
    print("A végeredmény:",number1 + number2)
elif muvelet =="*":
    print("A végeredmény:",number1 * number2)
elif muvelet == "/":
    print("A végeredmény:",number1 / number2)
elif muvelet == ":":
    print("A végeredmény:",number1 / number2)
elif muvelet == "-":
    print("A végeredmény:", number1 - number2)

szam = int(input("Mondj egy számot:\n"))
if szam > 0:
    print("A szám nagyobb 0-nál.")
elif szam == 0:
    print("A szám egyenlő 0-val.")
else:
    print("A szám nem nagyobb 0-nál.")