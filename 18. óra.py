import random


def negyzetelo():
    x = 1
    while True:
        yield x * x # return csak nem breakel
        x += 1
def paros(par_list):
    for i in par_list:
        if i % 2 == 0:
            yield i

def feladatok():
    for i in negyzetelo():
        if i > 1024:
            break
        print(i)

feladatok()
list = []
while len(list) < 20:
    szam = random.randint(1, 100)
    if not list.__contains__(szam):
        list.append(szam)
print("Az eredeti lista:", list)
for i in paros(list):
    print(i, end=" ")