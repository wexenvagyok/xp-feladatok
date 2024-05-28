#Írjon függvényt, amely a másodpercet átszámítja órává.
#A függvény bemenete egy egész szám, amely másodperceket jelenti. A kimenet egy valós szám, a bemenet átalakítva óra értékre.

masodperc = int(input("Adj meg egy számot (mp): "))

def atvalto(masodperc):
    ora = masodperc / 3600
    return ora

ora = atvalto(masodperc)
print(f"{masodperc} másodperc az {ora} óra.")