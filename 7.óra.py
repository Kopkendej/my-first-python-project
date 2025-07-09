"""#lista
list = [1,2,3,4,5,6,7,8,"logiscool"]
print(list) #listásan irja ki
print(*list) #letisztultan irja ki
print(type(list))
#index
print(list[8]) #ki irja a 9-id elemét(indexben az a 8)
print(list[-1]) #hátulról számulunk(az első szám az 1)
print(len(list)) #a lista hosszát mondja el

ab = len(list)
szam = 0
while ab > 0:
    print(list[szam])
    szam += 1

bevasarlolist = ["tej","tojás","csoki","chips","4"]
bevasarlolist.append("rtx 4090")
print(*bevasarlolist)
bevasarlolist.remove("tej")
print(*bevasarlolist)

bevasarlolist.pop(4) #csak számot torol
bevasarlolist.insert(3,"500g uránium") #beszúrás
print(bevasarlolist)"""
szamlista = []
szamlalo = 50
szam = 1
while szamlalo > 0:
    szamlista.append(szam)
    szam += 1
    szamlalo -= 1
print(szamlista)