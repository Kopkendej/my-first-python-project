import random
def rendezés():
    matrix2 = []
    for i in range(5):
        sor = []
        for j in range(4):
            sor.append(random.randint(1,100))
        matrix2.append(sor)
    for sor in matrix2:
        print(sor)
    print()
    matrix2.sort()
    for sor in matrix2:
        sor.sort()
        print(sor)
def orarend():
    orarend1 = []
    for i in range(5):
        orak = []
        for j in range(int(input("Hány órád lesz?\n"))):
            ora = input("Milyen órád lesz?\n")
            orak.append(ora)
        orarend1.append(orak)
    hetkoznap = ["Hétfő","Kedd","Szerda","Csütörtök","Péntek"]
    ind = 0
    for nap in orarend1:
        print(f"{hetkoznap[ind]}: {nap}")
        ind += 1
def csere():
    matrix = [[1, True, "Logiscool"],
             [3.14,666,False],
             ["string",1.234142, "Három"]]
    for sor in matrix:
        print(sor)
    sorIndex = int(input("Melyik sor?\n"))
    elemIndex = int(input("Melyik elem\n"))
    csereElem = input("Mire legyen kicserélve?")
    elemTipusa = input("Milyen tipusú ez az elem?\n")
    if elemTipusa == "str":
        csereElem == str(csereElem)
    elif elemTipusa == "int":
        csereElem = int(csereElem)
    elif elemTipusa == "float":
        csereElem = float(csereElem)
    elif elemTipusa == "bool":
        csereElem = bool(csereElem)
    matrix[sorIndex][elemIndex] = csereElem
    print()
    for sor in matrix:
        print(sor)

def feladatok():
    #rendezés()
    orarend()
feladatok()