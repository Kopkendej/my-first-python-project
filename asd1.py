def elsof(b):
    list = []
    if len(b) > 1:
        list.append(b[:1])
        list.append(b[-2:])
    print("".join(list))
def masodikf(a):
    lista = list(a)
    for i in range(len(a)):
        if a[i] == a[0]:
            lista[i] = "$"
    print("".join(lista))
def harmadikf(q):
    karakterek = {}
    for i, karakter in enumerate(q):
        if karakter in karakterek:
            return karakter, karakterek[karakter]
        else:
            karakterek[karakter] = i
    return None



def negyedik():
    matrix = [[1,2,3],
              [3,4,5],
              [6,7,8]]
    lista = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            lista.append(matrix[i][j])
    print(lista)
def negyedik1():
    matrix = [[1, 2, 3],
              [3, 4, 5],
              [6, 7, 8]]
    lista = []
    for i in matrix:
        for ertek in i:
            lista.append(ertek)
        return lista


def otodikf(x,t):
    tuplea = []
    for i in range(len(x)):
        if x[i] != t:
            tuplea.append(x[i])
    x = tuple(tuplea)
    print(x)



def main():
    #elsof("almafx")
    #masodikf("restart")
    #harmadikf("asds")
    #harmadik2("asdgfhnfdgvd")
    #negyedik1()
    x = (1,2,3,"a","b","c","a")
    otodikf(x,"a")
main()