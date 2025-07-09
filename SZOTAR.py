#keys(),values(),items()
dictionary = {"cat": "Katze", "dog": "Hund", "horse": "Pferd"}
for szo in dictionary:
    print(szo, "--->",dictionary[szo])
#keys()-kulcsok halmaza keys
for kulcs in dictionary.keys():
    print(kulcs)
# values()-értékek halmaza
for ertek in dictionary.values():
    print(ertek)
print(dictionary.items())
szamok = {1:1234,2:7231486,3:283947}
print("Legnagyobb", max(szamok.values()))
print("Legkisebb",min(szamok.values()))
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
for dic in (dic1,dic2,dic3):
    dic4.update(dic)