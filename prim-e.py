def prim_e(szam):
    if szam <= 1:
        return False
    for i in range(2, int(szam ** 0.5) + 1):
        if szam % i == 0:
            return False
    return True
szam = int(input("Adj meg egy számot: "))
if prim_e(szam):
    print("Ez egy prím szám.")
else:
    print("Ez nem prím szám.")