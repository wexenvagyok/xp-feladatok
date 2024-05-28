#Készítsen programot amely összeadja a bekért számokat 0 végjelig!
szamLista = []

bekert = 1
i = 0

while bekert > 0 : 
    bekert = int(input("Adj meg egy számot: "))
    i = bekert + i
    if bekert == 0:
        break
    else:
        szamLista.append(bekert)

#print(szamLista)

osszeadas = sum(szamLista)
print(f"A számok összeadva: {osszeadas}")