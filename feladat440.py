#Kérjen be két számot.
#Állapítsa meg, hogy a 0 értéktől azonos mértékkel térnek-e el.

elsoSzam = float(input("Add meg az első számot: "))
masodikSzam = float(input("Add meg a második számot: "))

if elsoSzam == masodikSzam:
    print("A két szám ugyanolyan mértékben tér el.")
else:
    print("A két szám nem azonos mértékben tér el.")
