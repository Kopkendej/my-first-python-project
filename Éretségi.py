import random
felso_hatar = int(input("Egy számot kell kitalálnod 1 és az általad megadott felső határérték\nközött.\nAdd meg a határértéket!"))
melyik_szam = random.randint(1 , int(felso_hatar))
def feladat(proba):
    tipp = int(input("Melyik számra gondoltam? (kilépés: -1)"))

    if melyik_szam == tipp:
        print(f"Eltaláltad",proba, "próbálkozásból!")
    elif tipp == int((-1)):
        print("Sajnálom! A kitalálandó szám a", melyik_szam ,"volt.")
    else:
        if tipp > int(melyik_szam):
            print("Sajnos nem talált!\nKissebb számra gondoltam!\n ")
            proba += 1
            feladat(proba)
        else:
            print("Sajnos nem talált!\nNagyobb számra gondoltam!\n ")
            proba += 1
            feladat(proba)
feladat(1)