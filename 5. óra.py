"""szam1 = float(input("Első szám:"))
szam2 = float(input("Második szám:"))
szam3 = float(input("Harmadik szám:"))
if szam1 > szam2:
    if szam3 > szam1:
        print("Legnagyobb szám:")
    elif szam1 > szam3:
        print("Legnagyobb szám:")
    else:
        print("Ugyan akkora az első és a harmadik számod")
#elif szam2 > szam1:
i = 0;
for _ in range(5):
    print("szia")
print("");
i = 0
while i < 5:
    print("szia")
    i += 1
print("Ez hányadik óra?\n a) 1. óra\n b) 2. óra\n c) 3. óra")
valasz = input("A válaszod: ")
while valasz != "b":
    print("Nem nyert! Próbáld újra!")
    valasz = input(print("Válaszod:"))
print("Gratulálok! Nyertél!")"""
import random

megfejtés = random.randint(1,100)
probak = int(input("Mennyiszer lehessen próbálkozni?\n"))
tipp = 0
while probak > 0 and tipp != megfejtés:
    tipp = int(input("Tipp:\n"))
    if tipp > megfejtés:
        print("A megfejtés kisebb.")
    elif tipp > megfejtés :
        print("A megfejtés nagyobb.")
    probak -= 1
    print(probak, "Próbálkozásod maradt!")
if tipp == megfejtés:
    print("Gratulálok! Nyertél!")
else:
    print("Nem sikerült! Vesztettél!")