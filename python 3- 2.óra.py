import pprint

student_data = {
    'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
    'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
    'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
    'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
    }
lyo_student_data = {} # Sara, David, Surya
#print(student_data.items())
for kulcsSzo, ertek in student_data.items():
    if ertek not in lyo_student_data.values():
        lyo_student_data[kulcsSzo] = ertek
student_data = lyo_student_data
print(student_data)
pprint.pprint(student_data)
allatok = {"foka":"dagadt","oposszum":"király","cica":"cuki","mokus":"Szandi","csikohal":"fiu szul"}
allatok_lista = list(allatok)
print(allatok_lista)
def hibakezeles():
    szam = input("Adj meg egy számot: ")
    if szam.isdecimal():
        szam = int(szam)
        print("A szám fele:", szam/2)
    else:
        print("Haló! Ez nem lesz jó")
def reciprok():
    try:
        szam = int(input("Adj meg egy számot:"))
        print("A szám reciproka:", 1/szam)
    except ValueError:
        print("Hiba Rossz érték")
    except ZeroDivisionError:
        print("Hiba! Nullával probaltal osztani!")
    except:
        print("ismeretlen hiba tortént")
def hibafelismeres():
    #print(5/0) nullával nem lehet osztani- ZeroDivisionError

    #szám = int("szám") ez egy szoveg nem lehet int-be tenni
    #print(szám)

    list= [1,2,3,4,5]
    #print(list[2.5]) az nem egész szám

    tuple_list = (1,2,3,4,5)
    #tuple_list.append(6) ez egy tupple nem lehet igy hozzá adni
    #for in i range(1,11): - i és in felcserélése
        #print(i)

def szamcsekkolo():
    szam = int(input("Kérek egy számot: "))
    if szam > 0:
        print("Pozitiv")
    elif 0 > szam:
        prin("Negativ") #nem mindig érjuk, hiába hibás(ez egy Interpeter nyelv)
    else:
        print("Nulla")
    # A Python interpreter(mint pl.: JavaScript)
    # Interpreter(tolmács):minden futás előtt fordit,kell hozzá interpeter program,gyors
def gyakorlo():
    try:
        szam = int(input("Kérek egy számot: "))
        print(szam / szam)
    except ValueError:
        print("Hiba Rossz érték")
    except ZeroDivisionError:
        print("Hiba! Ez egy onmagával valo osztás és nullával nem lehet osztani!")
    except Exception:
        print("Hiba:",Exception)
def main():
    #hibakezeles()
    #reciprok()
    #hibafelismeres()
    #szamcsekkolo()
    gyakorlo()
main()

