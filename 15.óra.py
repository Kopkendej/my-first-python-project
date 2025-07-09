"""Alap sztori:anya elküldött urániumért és megtalált az fbi és menekülni kell a baglyoktól és megbizott a nav hogy el kell rontani a gartic phonozását a csoportnak
kijárat: jelszó kell(titkosított, sorrend)
szobák/számítógépek: a jelszók karaktereit rejtik
időkorlát
inventory"""
jelszo = "jelszo123"
inventory = []
megjart_szobak = []
megtalat_karakterek = []
import random
win = False
import jumpscare
jumpscare
pénz = 15000
ido = 10
print("Alap sztori:anya elküldött urániumért és megtalált az fbi és menekülni kell a baglyok-\ntól és megbizott a nav hogy el kell rontani a gartic phonozását a csoportnak.\n Ehhez megkell keresned a fő computer hohy fejtsd a gartic phone link jelszavát.\n 6 szobát kell megjárnod hogy megtaláld a jelszót.\n Ha nem fejted meg időben, akkor el kapnak a baglyok!")
input("Nyomj Entert a kezdéshez!")
for i in range(ido):
    if ido < 1 or win == True:
        break
    print("Eddig történtek:")
    print(ido,"lépésnyi időd van hátra!")
    print("A tatyód tartalma:",inventory)
    print("Itt jártál már:", set(megjart_szobak))
    print("Megtalált jelszó karakterek:",megtalat_karakterek)
    szoba_input = input("Hova akarsz menni? (1-6)\n")
    if szoba_input == "1":
        print("Vagyonod:", pénz)
        print("Belépsz a szobába, körül nézel és találsz egy kék francia sajtot. Megeszed?")
        sajt = input("Megeszed? (IGEN/NEM)")
        if sajt.upper() == "IGEN":
            print("Megeszed a sajtot de képzeld allergiás vagy rá. Szívás.Ha van pénzed tud-\nsz venni allergia elleni gyógyszert 5000ft-ért, egyébként vesztesz 1 lépésnyi időd.")
            gyogyszer = input("Megveszed: (IGEN/NEM)")
            if pénz >= 5000 and gyogyszer.upper() == "IGEN":
                print("Megeszed, beveszed, meggyógyulsz.")
                pénz -= 5000
            else:
                print("-1 lépésnyi idő (nem volt rá pénzed vagy NEM-et irtál vagy hülyeséget irtál)")
                ido -= 1
        elif sajt.upper() == "NEM":
            print("as")
            print("Nem eszed meg, nem kivánod(Jól tetted).")
        else :
            print("Hallgatás beleegyezés.")
            print("Megeszed a sajtot de képzeld allergiás vagy rá. Szívás.Ha van pénzed tud-\nsz venni allergia elleni gyógyszert 5000ft-ért, egyébként vesztesz 1 lépésnyi időd.")
            gyogyszer = input("Megveszed: (IGEN/NEM)")
            if pénz >= 5000 and gyogyszer.upper() == "IGEN":
                print("Megeszed, beveszed, meggyógyulsz.")
                pénz -= 5000
            else:
                print("-1 lépésnyi idő")
                ido -= 1
        megjart_szobak.append(1)
        ido -= 1
        input("\nNyomj Entert hogy tovább menj.")
    elif szoba_input == "2":
        print("Egy szerencsekereket találsz, kipróbálod?")
        print(''' 
                     -10%
                  RIP    +100%
               -300%       +200%
              +5%     ..    -100%
              -200%         +10%
                +20%      +300%
                    -200%
                    ''')
        if input("SPIN (enter)") == "":
            game = random.randint(1, 12)
            szazalekok = [-0.1, 2, 3,-2,1.1,4,-3,1.2,-2,0.5,-3,"RIP"]
            if szazalekok[game] != "RIP":
                pénz *= szazalekok[game]
                print(szazalekok[game])
            else:
                ido = 0

        megjart_szobak.append(2)
        ido -= 1
        input("\nNyomj Entert hogy tovább menj.")
    elif szoba_input == "3":
        print('Belépsz a szobába és meglátsz egy táblát.A táblára a következő van fel írva:\n "Ki hozta létre a Logiscoolt?" \n a) Isten b) Németh András c) Csitári Gyula \n A tábla alatt egy lelakatolt'
              'láda található, a kinyitásához add meg a helyes választ.')
        opciok = input("A válaszod: ")
        if opciok.lower() == "a" or opciok.lower() == "c":
            print("A válaszod... JÓ a lakat kinyílt. A dobozban megtalálsz egy kulcsot!")
            inventory.append("kulcs")
        else:
            print("Helytelen! Elsötétül a kép és a szobából kint találod magad.")
        megjart_szobak.append(3)
        ido -= 1
        input("\nNyomj Entert hogy tovább menj.")
    elif szoba_input == "4":
        print("Ebben a szobában található a gartic phone fő komputer-re")
        jelszo_dontes = input("Be írod a jelszót? (IGEN/NEM)")
        while ido > 0 and jelszo_dontes.upper() == "IGEN":
            jelszo_tipp = input("Mi a jelszó?: ")
            if jelszo_tipp == jelszo:
                 win = True
            else:
                print("Helytelen!")
                ido -= 1
                jelszo_dontes = input("Be írod a jelszót? (IGEN/NEM)")
        megjart_szobak.append(4)
        ido -= 1
        input("\nNyomj Entert hogy tovabb menj.")
    elif szoba_input == "5":
        print("Egy őr állja a szoba útját, aki csak akkor enged be, ha van kulcsod...vagy egy kis pénzed...")
        if "kulcs" in inventory:
            print("Az őr ki nyitja neked az ajtót és belépsz egy szobába. A falon meglátsz valamit felfirkálva vérrel: SZEMÜVEG KELL")
            if "szemüveg" in inventory:
                print("Felveszed a szemüveged, és a firka mellett ezt látod: jelszo123")
            else:
                print("Nincs nálad szemüveg, dee pont melletted van egy bódé, és árulnak SZEMÜVEGET")
                if pénz >= 7000:
                    print("Megvetted.Felveszed a szemüveged, és a firka mellett ezt látod: jelszo123")
                else:
                    print("Ssss... keresd a 6. szobába")
        else:
            print("Sajnos nincs kulcsod.")
            or_dontes = input("Lefizetted az őrt? (IGEN/NEM)")
            if or_dontes.upper() == "IGEN" and pénz >= 8000:
                print("Az őr ki nyitja neked az ajtót és belépsz egy szobába. A falon meglátsz valamit felfirkálva vérrel: SZEMÜVEG KELL")
                if "szemüveg" in inventory:
                    print("Felveszed a szemüveged, és a firka mellett ezt látod: jelszo123")
                else:
                    print("Nincs nálad szemüveg, dee pont melletted van egy bódé, és árulnak SZEMÜVEGET")
                    if pénz >= 7000:
                        print("Megvetted.Felveszed a szemüveged, és a firka mellett ezt látod: jelszo123")
                    else:
                        print("Ssss... keresd a 6. szobába")
            else:
                print("Csóró vagy!")

        megjart_szobak.append(5)
        ido -= 1
        input("\nNyomj Entertt hogy tovább menj.")
    elif szoba_input == "6":
        print("Be lépsz a szobába és egy ruhás szekrényt látsz.Ki nyitod és ki veszel egy szemüveget.")
        inventory.append("szemüveg")
        megjart_szobak.append(6)
        ido -= 1
        input("\nNyomj Entert hogy tovabb menj.")

        if ido > 0:
            print("Gratulálunk! Sikeresen beléptél a gartic phoneba és széttrollkodtad mielőtt\n még elkaptak volna a baglyok!")
        else:
            print("Megérkeztek a baglyok. VÉGED VAN!!")
    #if szoba_input == "turtle":