import math
import random


def fuggveny(x):
    if x > 0:
        print("asd")
        x -= 1
        fuggveny(x)
#fuggveny(10)
def visszaszamlalo(i):
    if i > -1:
        print(i)
        i -= 1
        visszaszamlalo(i)
#visszaszamlalo()

def faktorialis(n):
    if n > 0:
        return n * faktorialis(n-1)
    else:
        return 1
#print(faktorialis(szamom))
import math
print(math.factorial(5))
szam = random.randint(1 , 100)
life = 3

def talaldki():
    hp = 5
    szam = random.randint(1, 100)
    tipp = input("Találd ki a számot:")
    while szam != tipp and hp > 0:
        if szam > tipp :
            print("Nagyobb")

        else:
            print("Kisebb")
        hp -= 1
        tipp = input("Találd ki a számot:")
    if hp > 0:
        print("Jó válasz")
    else:
        print("Vesztettél a megoldás:", szam)

def bevitel():
    x = int(input("Kérek egy pozitív számot:\n"))
    if x< 0:
        print("Pozitív számot kérek.")
        bevitel()
    else:
        print("Ez egy pozitív szám")
bevitel()


