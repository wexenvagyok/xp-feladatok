#Kérjen be egy számot. Ha 50-nél kisebb kérje újra.

while True:
    szam = szam = float(input("Adj meg egy számot: "))
    if szam >= 50:
        break
    else:
        print("A megadott szám 50-nél kisebb.")

print("A megadott elfogadva.")
