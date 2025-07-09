import random


def Tesco():
    termek = ["airfryer", "rotációs kapa", "uránium", "karcher porszívó", "PS5", "ketchup", "tojás"]
    ar = [20000, 250000, 1, 150000, 240000, 700, 999]
    kosar = []
    kosar_ar = []

    def Kisteso():
        TermékDarabSzam = int(input("Hány dologra verje el a pénzt kistesó?\n"))
        for i in range(TermékDarabSzam):
            rand = random.randint(0, len(termek)-1)
            kosar.append(termek[rand])
            kosar_ar.append(ar[rand])
            print(f"{kosar[i]}-{kosar_ar[i]}")
        print(sum(f"Ennyit vert el kistesó:{sum(kosar_ar)}"))
        print(sum(f"Ennyit vert el kistesó:{min(kosar_ar)}"))
    Kisteso()
def Szum(lista):
    total = 0
    for ar in kosar_ar:
        total += ar
    return total
def MAX():
    legdragabb = 0
    for ar in kosar_ar:
        if legdragabb < ar:
            legdragabb = ar
    return legdragabb
    max_valtozo = MAX()
    print(f"A legdrágább volt(saját fuggveny):{min_valtozo}")
MAX()
