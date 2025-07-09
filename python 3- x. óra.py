# adatok tárolása: lista, tuple, változó, mátrix
#dictionary (szótár)
szotar = {"uránium": "uranium", "alma": "city"} # {key : value, key2}
szotar1 = {"Béla": "911", "Erzsébet": "362066638", "Máté": "3620213848"}
ures_szotar = dict()
print(ures_szotar)
print(szotar1["Máté"])
nevek = {"Józsi": "Blaha", "Máté": "Észak-Korea","Szofi":"Debrecen","máté":"ROMÁNIA"} #nincs diplikálás
print(nevek)
bikini_fenek = {"Spongyabob": "ananász","Patrik":"kő","tunacsáp": "moai","szandi":"valami uveg cucc"}
lakok = ["Spongyabob", "Szandi", "Plankton"]
#print(bikini_fenek["Plankton"])
"""for i in range(len(lakok)):
    if lakok[i] in bikini_fenek:
        print(lakok[i], ":",bikini_fenek[lakok[i]])
    else:
        print(lakok[i], "nincs benne a szotarban")"""
haziallat = {
             "név":"Leia",
             "faj":"kutya",
             "kedvenc kaja":"popcorn",
             "Hobbi":"arcon harapás"
             }
haziallat["kedvenc kaja"] = "kaaaja"
print(haziallat)
haziallat.update({"Kedvenc étel": "popcorn"})
haziallat["Alfaj"] = "francia bulldog"
print(haziallat)
haziallat.update({"szarmazik" : "zedorszag"})
print(haziallat)
del haziallat["Hobbi"]
print(haziallat)
haziallat.popitem() #torli az utso adat part
print(haziallat)
for i in range(len(haziallat)):
    print(i)