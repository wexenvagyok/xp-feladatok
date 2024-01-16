lista = []
glukoz = [6,12,6]

szen = int(input("Add meg a széntartalmat: "))
hidrogen = int(input("Add meg a hidrogéntartalmat: "))
oxigen = int(input("Add meg az oxigéntartalmat: "))

lista.append(szen)
lista.append(hidrogen)
lista.append(oxigen)

if lista == glukoz:
    print("A képlet alapján lehet glükóz.")
else:
    print("A képlet alapján nem lehet glükóz.")
