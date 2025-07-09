#függvények pl.: print(), set(), int(), range()
def első_python_függvényem(): # <-- fügvény
    print("Szia!")
első_python_függvényem() # <-- fügvény meghívása
def primszame():
    szam = int(input("Adj meg egy számot"))
    prim = True
    for i in range(2,szam):
        if szam % i == 0:
            prim = False
    if prim:
        print("Ez egy prímszám")
    else:
        print("Ez nem egy prímszám")
#primszame()
def ParameterFuggveny(parameter):
    print(parameter)
#ParameterFuggveny("Ez egy jel")
def primszamee(szam2):
    szam = (szam2)
    prim = True
    for i in range(2,szam):
        if szam % i == 0:
            prim = False
    if prim:
        print("Ez egy prímszám")
    else:
        print("Ez nem egy prímszám")
primszamee(21)
def returnfug(szam):
    if szam >= 0:
        return szam
    else:
        return -szam
print(returnfug(-105))