
"""if szam & 1 == 0:
    print(f"a szám páros")
def shiftelés(szam):
    print(szam)
    print(bin(szam))
    print(szam << 2)
    szam <<=1"""

def átalakito():
    szam =input("Adj meg egy számot")
    valasz= input("Add meg hogy milyen számrendszerben kéred.(bin(2),oct(8),hex(16)")
    if valasz == "bin":
        print(bin(int(szam)))
    elif valasz == "oct":
        print(oct(int(szam)))
    elif valasz == "hex":
        print(hex(int(szam)))
átalakito()
def csere(a,b):
    
csere(5,10)