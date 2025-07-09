"""jelszo = input("Kérek egy jelszót")

if len(jelszo) >= 8 and len(jelszo) <= 16:
    kisbetu = 0
    nagybetu = 0
    szam = 0
    list = ["@", "_", "#", "$", "&", "/"]
    karakter = 0
    for i in jelszo:
        if i.islower():
            kisbetu += 1
        if i.isupper():
            nagybetu += 1
        if i.isdigit():
            szam += 1
        if i in list:
            karakter += 1
        if kisbetu == 0:
            print("Rossz jelszó! Beragadt Caps Lock")
        if nagybetu == 0:
            print("Rossz jelszó! Nincs nagybetű.")
        if szam == 0:
            print("Rossz jelszó! Nincsen szám. Pusztuljááá :0")
        if karakter == 0:
            print("Rossz jelszó! No speckó karakter.")
else:
    print("Rossz jelszó! Nem megfelelő a jelszó hossza")"""
list = []
for i in range(5):
    list.append(input("Szó: "))
for i in list:
    print(i, end=" ")
for i in list:
    print(i, sep=" ")