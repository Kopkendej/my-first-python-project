eletkor = 101
print("név",eletkor)
asd = "Kende a nevem "
dsa = "12 éves vagyok."
print(asd + dsa)
#Új anyag ELÁGAZÁS
print("Ez hányadik óra?\n a) 1. óra\n b) 2. óra\n c) 3. óra")
valasz = input("A válaszod: ")
if valasz == "c)":
    print("Gratulálok! Nyertél!")
else:
    print("Nem nyert! Helyes válasz c)")
    #kisebb nagyobb
    szam1 = int(input("Add meg az első számot:\n")) # str -> int()
    szam2 = int(input("Add meg a második számot:\n")) # str -> int()
    if szam1 > szam2:
        print("Az első szám a nagyobb.")
    elif szam2 > szam1:
        print("A második szám a nagyobb.")
    else :
        print("A kettő szám ugyan akkora.")
        #if-nél 1db if és 1db else De elif ből végtelen
