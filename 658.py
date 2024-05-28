#Írjon programot, amely bekér egy karakterláncot, majd kiírja hány darab „a” és „e” betű van benne!

karakterlanc = input("Add meg a karakterláncot: ")
aMennyiseg = 0
eMennyiseg = 0

for karakter in karakterlanc:
    if karakter == 'a' or karakter == 'A':
        aMennyiseg += 1
    if karakter == 'e' or karakter == 'E':
        eMennyiseg += 1

print(f"Az \"a\" karakterek száma: {aMennyiseg} és az \"e\" karakterek száma: {eMennyiseg}")