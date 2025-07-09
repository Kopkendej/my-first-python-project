
def bevezeto():
    list = []
    for i in range(100):
        if i % 2 == 0:
            list.append(i)
    print(list)

    menobblista = [i for i in range(100)]
    print(menobblista)
    menobbparoslista = [i for i in range(100) if i % 2 == 0]
    print(menobbparoslista)
def matrix():
    import random
    matrix = [[i for i in range(10) if i % 2 == 0] for i in range(3)]
    for sor in matrix:
        print(sor)
    matrix = [[random.randint(1,100) for i in range(10)] for i in range(3)]
    for sor in matrix:
        print(sor)
def onallo():
    import random
    hotel = []
    for i in range(3):
        epulet = []
        for j in range(3):
            emelet = []
            for y in range(3):
                szoba = random.randint(0,1)
                emelet.append(szoba)
            epulet.append(emelet)
        hotel.append(epulet)
    for sor in hotel:
        print(sor)
    tomoritetthotel = []
def rovidebb():
    import random
    hotel = [[[random.randint(0, 1) for a in range(3)] for b in range(3)] for c in range(3)]
    for sor in hotel:
        print(sor)
def csomagok():
    import PIL import Image
    im = Image.open()

def feladatok():
    #bevezeto()
    #matrix()
    #onallo()
    #rovidebb()
    csomagok()
feladatok()
