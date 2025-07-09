#legkisebb közös töbszörös
szam1 = int(input("Első szám:")) #2
szam2 = int(input("Második szám:")) #6
if szam1 < szam2:
    lkt = szam1
else:
    lkt = szam2

while(lkt % szam1 == 0 and lkt % szam2 == 0):
    lkt +=1
#print("A",szam1 "és a ", szam2,"legkisebb közös töbszöröse:", lkt)
print(f"A {szam1} és a {szam2} legkisebb közös töbszöröse: {lkt}")