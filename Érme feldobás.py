import random
def feldobas():
     return random.randint(1,2)
def dobásokpenzstimulálása():
    for i in range(5):
        eredmeny = feldobas()
        if eredmeny == 1:
            print("Fej")
        else:
            print("Irás")
def bekerés():
    valasztas = input("Válasz (Fej/Irás):\n")
    feldobas()
    eredmeny = feldobas()
    if eredmeny == 1:
        eredmeny = "Fej"
    else:
        eredmeny = "Irás"
    if valasztas == eredmeny:
        print("Nyertél")
    else:
        print("Vesztettél")

dobásokpenzstimulálása()
bekerés()