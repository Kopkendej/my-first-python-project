import random


def bevezeto():
    valtozo = 5
    list [1,2,3,4,5]
    print(list)
    print(list[2])
    #mátrix - két dinemziós lista
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    for sor in matrix:
        print(sor)
        print()
    print(matrix[-1][-2]) # 1.a sor indexe 2. az elem indexe
def MatrixKeszito():
    matrix = [] #3x3,1-9 számokkal
    for i in range(3):
        sor = []
        for j in range(3):
            sor.append(j)
        matrix.append(sor)
    for sor in range():
        print(matrix)
    print()
def matrix2():
    Matrix2 = [] # 5x4 1-100 kozotti rANDOM SZÁM
    for m in range(5):
        sor = []
        for n in range(4):
            sor.append(random.randint(1,100))
        Matrix2.append(sor)
    for sor in Matrix2:
        print(sor)
    print()
def oszlop():
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    for i in range(len(matrix)):
        print(matrix[i][0])
def kaputelefon():
    kaputelefon = [[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   ["*",0,"#"]]
    for sor in kaputelefon:
        print(sor)

def feladatok():
    #bevezeto()
    #MatrixKeszito()
    #matrix2()
    #oszlop()
    #kaputelefon()
feladatok()