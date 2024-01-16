#441: Kérjen be egy számot. Állapítsa meg, hogy páros vagy páratlan.

szam = float(input("Adj meg egy számot: "))

if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")
