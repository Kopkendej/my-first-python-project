"""#novekvo sorrenlist = [1,4,3,7,2,6,5,8]
list.sort()
print(list)
rendezett_list = sorted(list)#nem módosítja az eredetit
print(rendezett_list)
list = [61, 5, 6, 28, 87, 52, 89, 51, 86, 29, 93, 26, 99, 16, 36, 53, 47, 95, 18, 54, 62, 37, 34, 11, 75, 90, 88, 24, 72, 76, 55, 44,  3, 50, 35, 17, 94,  7, 31,100, 42, 43, 74, 83, 82,  4, 10]
lista = [5, 9, 62, 79, 17, 68, 54, 50, 60, 89, 29, 41, 83, 77,  3, 86, 56, 13, 26, 52, 98, 81, 82, 74, 55, 66, 92, 61, 30, 37, 57, 91,  2, 71, 93, 35, 33, 24,100, 19, 65, 95, 90, 38, 88, 31, 80, 70, 25, 39, 15, 85, 42, 94, 11, 76, 32,  7, 48]
kozos_elemek = []
for i in list:
    for j in lista:
        if i == j:
            kozos_elemek.append(i)
print(kozos_elemek)
print(len(kozos_elemek))
#számelemekből szám
szam = [512,37,8]
egész_szám = ""
for i in szam:
    egész_szám += str(1)
print(egész_szám)"""
#bolt
termékek = ["tej","instantpalacsintapor","mirelit sárkány","süsü házi eledel"]
ár = [1000,500,120000,23000]
keret = 5000
keret_lista = []
for i in range(len(ár)):
    if ár[i] <= keret:
        keret_lista.append(termékek[i])
print(keret_lista)
