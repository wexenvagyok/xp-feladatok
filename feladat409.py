#Olvassunk be egy valós számot, és döntsük el, hogy szigorúan 10 és 20 közé esik-e!ű

szam = float(input("Valós szám ellenőrző\nAdd meg a számot: "))

if szam <= 20 and  szam >= 10:
    print("A szám tíz és húsz között van.")
else:
    print("A szám nincs tíz és húsz között.")
    
