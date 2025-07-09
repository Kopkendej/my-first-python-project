#akasztófa
puzzle = "Logiscool"
megoldás = "*********"
hp = 10
helytelen_betűk = []
helyes_betűk = []
while hp > 0 and megoldás != puzzle:
    print(megoldás)
    tipp = input("Tipped: ")
    if len(tipp) == len(puzzle):
        print("Megpróbáltad tippelni az egész puzzlet. A megoldás...")
        if tipp == puzzle:
            print("Helyes!")
            megoldás = puzzle
        else:
            print("Helytelen!")
            hp -= 1
            print(hp, "Próbálkozásod maradt")
    else:
        talált = False
        for i in range(len(puzzle)):
            if puzzle[i] == tipp:
                megoldás_list = list(megoldás)
                megoldás_list = tipp
                megoldás = "".join(megoldás_list)
                talált = True
        if not talált:
            hp -= 1
            helytelen_betűk.append(tipp)
            print("Helytelen!")
            print(hp, "próbálkozásod maradt.")
        else:
            helyes_betűk.append(tipp)
        print("Helyes lista:", helyes_betűk)
        print("Helytelen lista:", helytelen_betűk)
if hp > 0:
    print("Gratulálok nyertél!")
else:
    print("Nem sikerült! Próbáld újra!")
