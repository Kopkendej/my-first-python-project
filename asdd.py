
def asd():
    szavak = ["lovacska","ketto","8.osztaly","spongyabob","pitagorasztetel","FiZiKa"]
    hossz = []
    szotar = {}
    for i in range(len(szavak)):
        hossz.append(len(szavak[i]))
        szotar[szavak[i]] = hossz[i]
    print(hossz)
    print(szotar)
    print(max(szotar.values()))
asd()
def matriiiix():
    import pprint
    matrix= [[1,2,3,4,],
            [2,3,4,5,6,7],
            [3,1,4,4]]
    while(len(matrix[0]) != len(matrix[1]) or len(matrix[0]) != len(matrix[2]) or len(matrix[1]) != len(matrix[2])):
        while(len(matrix[0]) != len(matrix[1])):
            if len(matrix[0]) > len(matrix[1]):
                matrix[1].append(0)
            else:
                matrix[0].append(0)
        while (len(matrix[1]) != len(matrix[2])):
            if len(matrix[1]) > len(matrix[2]):
                matrix[2].append(0)
            else:
                matrix[0].append(0)
        while (len(matrix[0]) != len(matrix[2])):
            if len(matrix[0]) > len(matrix[2]):
                matrix[2].append(0)
            else:
                matrix[0].append(0)
    pprint.pprint(matrix)

    keresettszam = int(input("Add meg a szamot"))
    megvan = False
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            if matrix[i][j] == keresettszam:
                print(f"[{i}][{j}]")
                megvan = True
    if not megvan:
        print("A keresett szám nem találhato meg a listában")
matriiiix()