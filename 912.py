#Írjon függvényt, amely a másodpercet átszámítja perccé.
#A függvény bemenete egy egész szám, amely másodperceket jelenti. A kimenet egy valós szám, a bemenet átalakítva perc értékre.

masodperc = int(input("Adj meg egy számot (mp): "))

def atvalto(masodperc):
    perc = masodperc / 60
    return perc

perc = atvalto(masodperc)
print(f"{masodperc} másodperc az {perc} perc.")