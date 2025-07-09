#continue
for i in range(1,11):
    if i % 2 == 1:
        print(i)
for i in range(1,11):
    if i % 2 == 0:
        continue#a jelenlegi lefutást ugorja át
    print(i)
stringek = ["Logiscool" ,"",  "kutya","","majom"]
for f in stringek:
    if not f:
        continue
    print(f)
#del
stringek = ["Logiscool" , "" ,  "kutya", "", "majom"]
del stringek[-1]
print(stringek)
del stringek
#tuple
ures_tuple = ()   # lehet ures,nem lehet hozzá adni/torolni, biztonságos
tuple_lista = list(ures_tuple)
tuple_lista.append(False)
ures_tuple = tuple(tuple_lista)
print(tuple_lista)
stringek = ["Logiscool" , "" ,  "kutya", "", "majom"]
print(stringek[2:5])    # lista[mettől:meddig],lista[mettől:meddig:hányasával lépjen]
print(stringek[:5])     #  [0:5])
#slicing másolásv
stringek = ["Logiscool" , "" ,  "kutya", "", "majom"]
masolat = stringek
print(masolat)