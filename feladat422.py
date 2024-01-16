
#Van 10000 Ft-od. Elmész bevásárolni.
#Lehet kapni lisztet (300 Ft/kg), mézet (1000 Ft/kg), tej (200 Ft/l).
#A program olvassa be, hogy miből mennyit akarsz venni,
#és írja ki a fizetendő összeget. Ha több lenne a végösszeg annál,
#mint amennyi nálad van, akkor írja ki a program, hogy nincs elég pénzed.

penzed = 10000
liszt = 300
mez = 1000
tej = 200

lisztMennyiseg = int(input("Add meg mennyi lisztet szeretnél (kg): "))
mezMennyiseg = int(input("Add meg mennyi mézet szeretnél (kg): "))
tejMennyiseg = int(input("Add meg mennyi tejet szeretnél (l): "))

fizetendo = liszt*lisztMennyiseg + mez*mezMennyiseg + tej*tejMennyiseg

if fizetendo > 10000:
    print("Nincs elegendő pénzed.")
else:
    print("Sikeres vásárlás.")
