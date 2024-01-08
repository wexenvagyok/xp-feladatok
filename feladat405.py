elsoSzam = int(input("Add meg a két számot!\nAz első szám: "))
masodikSzam = int(input("A második szám:"))
#Kérjünk be két számot! Döntsük el, hogy a második osztója-e az elsőnek!
#Maradék nélkül?

if elsoSzam % masodikSzam == 0:
    print("A második szám osztója az elsőnek.")
else:
    print("A második szám nem osztója az elsőnek.")
