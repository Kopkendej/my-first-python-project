import os
def Txtkeszito(nev):
    fajl = open(nev+".txt","w") #név, művelet
    fajl.close()

def beirkalo(nev,cucc):
    asd = ("ahushdhashhxhahsxh")
    fajl = open(nev + ".txt","w")
    fajl.write(asd)
    fajl.close()

def hozzairkalo(nev,cucc):
    fajl = open(nev + ".txt", "a",encoding= "utf-8")
    fajl.write(cucc)
    fajl.close()
def beolvasas(nev):
    fajl = open(nev + ".txt", "r", encoding="utf-8") #read
    #print(fajl.read())
    sorok = fajl.readline()
    for sor in sorok:
        print(sor,end="")
    print(fajl.read(6))
    print(fajl.seek(0))
    fajl.close()
def multi(nev):
    fajl = open(nev + ".txt", "w+", encoding="utf-8")
    for i in range(11):
        fajl.write(str(i) + " ")
    fajl.seek(0)
    print(fajl.read())
    fajl.close()
def torlo(nev):
    os.remove(nev + ".txt")
def kereso(kereses,nev):
    fajl = open(nev + ".txt", "r+", encoding="utf-8")
    if kereses in fajl.read():
        print("A keresett cucc benne van a fájlban")
    else:
        print("A keresett cucc nincs benne a fájlban")
def nospace(elsofajl,masodikfajl):
    fajl = open(elsofajl + ".txt", "r+", encoding="utf-8")
    fájl = fajl.read().replace(" ","")
    asd = open(masodikfajl + ".txt","w")
    asd.write(fájl)
    print(fajl)
    fajl.close()
    asd.close()

Txtkeszito("én picifájlom")
#beirkalo("én picifájlom", "asd")
#("én picifájlom", "Ez a shrek egy mestermű")
#beolvasas("én picifájlom")
multi("én picifájlom")
#torlo("én picifájlom")
nospace("én picifájlom","asd")