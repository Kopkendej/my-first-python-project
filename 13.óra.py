"""list = []
for i in range (10):
    list.append(int(input("Írj egy számot: ")))
pozitív = 0
negatív = 0
páros = 0
páratlan = 0
nulla = 0
for i in list:
    if i > 0:
        pozitív += 1
    elif i < 0:
        negatív += 1
    else:
        nulla += 1
    if i % 2 == 0:
        páros += 1
    else:
        páratlan += 1
print(f"Pozitív szám(ok): {pozitív}\nNegatív szám(ok): {negatív}\n Nulla szám(ok): {nulla}\n Páros szám(ok): {páros}\n Páratlan szám(ok): {páratlan}")

szamok = [1, 2, 3, 4, 5, 6, 5, 4, 5, 6, 1, 0, 1, 3]
halmaz = set(szamok)
egyedi_szamok = halmaz
print(egyedi_szamok)"""
minden_lista = [2, 3, 3.14, "Bob", -2, 3, 42, True, "null", False, 0]
szam_lista = []
for i in minden_lista:
    if type(i) == int:
        szam_lista.append(i)
print(szam_lista)

