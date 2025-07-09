#bináris műveletek 1= igaz, 2 = hamis
print(bin(42))
#2048 , 1024,512,128,64,32,16,8,4,2
#1011011001 ---> 1+8+16+64+128+512
print(sum([1,8,16,64,128,512]))
print(bin(729)) #0b bináris jelolo

print(hex(1264830)) #hexadecimális
print(oct(1264830))
#10-es ergo decimális
szam1 = 6 #110
szam2 = 42 #101010
print(szam1 &szam2)
#OR(UNIO)
print(szam1|szam2)
#metszett
# XOR
print(szam1^szam2)
#0010  --> 6
#1110--> 14
#csak az egyikben van meg
print(~szam1)
#0010  --> 6
print(~szam2)
#1110--> 14
#*-1+(-1)
print(szam1 >> 2)
#0010  --> 6
#1110--> 14
# 110 >> 11>> 1
