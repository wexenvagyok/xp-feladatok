nev = input("Személy neve: ")
telepules = input("Település: ")
lakcimUtca = input("Lakcím (utca): ")
lakcimHazszam = int(input("Lakcím (házszám): "))
szuletesiEv = int(input("Születési év:"))
szuletesiHonap = int(input("Születési hónap:"))
szuletesiNap = int(input("Születési nap:"))
fizetes = int(input("Fizetés:"))

print("182. Feladat")
print("Név: "+nev)
print("Település: "+telepules)
print("Cím: "+lakcimUtca+" "+str(lakcimHazszam))
print("Születés: "+str(szuletesiEv)+"-"+str(szuletesiHonap)+"-"+str(szuletesiNap))
print("Fizetés: "+str(fizetes))
#szerintem jónak kéne lennie, bár nálam valami baja van :(