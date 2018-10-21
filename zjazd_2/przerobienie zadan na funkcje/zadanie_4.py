def test_naleznosc():
    assert policz_naleznosc(1,2) == 2
    assert policz_naleznosc(0, 2) == 0
    assert policz_naleznosc(2, 0) == 0

cena_kg = 10
waga = 3 # float(input("Ile? "))

def policz_naleznosc(cena_kg, waga):
    naleznosc = cena_kg * waga
    return naleznosc

def wydruk(cena_kg, waga):
    naleznosc = policz_naleznosc(cena_kg,waga)
    out = f"""
    Cena: {cena_kg} PLN/KG
    Waga: {waga} KG
    Należnośc wynosi: {naleznosc} PLN
    """
    return(out)
    print(out)


wydruk(cena_kg,waga)
