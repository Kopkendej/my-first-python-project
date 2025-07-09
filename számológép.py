szam1 = int(input("Add meg az első számot:"))
muvelet = input("Add meg a muveletet:")
szam2 = int(input("Add meg az másaodik számot:"))
if muvelet == "+":
    print(szam1 + szam2)
elif muvelet == "-":
    print(szam1 - szam2)
elif muvelet == "/":
    print(szam1 / szam2)
elif muvelet == "*":
    print(szam1 * szam2)
else:
    print("Muveletet adj meg te idiota")