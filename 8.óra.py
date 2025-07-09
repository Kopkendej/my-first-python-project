# while
i = 0
while i < 100:
    print(i)
    i+= 1
# for
for j in range(100):
    print(j)
for i in range(10,100,2): #első medtől második meddig harmadik hányasával
    print(i)
for i in range(7,-20,-1):
    print(i)
for i in "logiscool":
    print(i)
for i in ["szia",1,True]:
    print(i)
list = []
for i in range(50):
    list.append(i)
print(list)
nevek = ["Máté", "Nimród", "Kende", "Balázs", "Áron", "Alex", "Iván", "Illés", "Vilko", "Szilárd"]
megtalálta = False
valasz = input("asdj egy nevet:\n")

for c in nevek:
    if c.upper()==valasz.upper():
        megtalálta = True
if megtalálta:
    print("Megvan a név a listában")
else:
    print("nincs ilyen a listában")