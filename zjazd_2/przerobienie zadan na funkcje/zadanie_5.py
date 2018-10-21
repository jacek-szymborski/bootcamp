def pobierz_dane():
    miasto_z = input("Skąd jedziesz?: ")
    miasto_do = input("Dokąd?: ")
    ile_km = float(input("Ile to km?: "))
    ile_pali = float(input("Ile spala Twój samochód na 100km?: "))
    cena_paliwa = float(input("Ile kosztuje litr paliwa?: "))
    return miasto_z, miasto_do, ile_km, ile_pali, cena_paliwa

def policz_koszt(ile_km, ile_pali, cena_paliwa):
    koszt_paliwa = cena_paliwa * ile_pali * (ile_km / 100)
    litry = ile_km / 100 * ile_pali
    return koszt_paliwa, litry

def wydrukuj(miasto_z, miasto_do, ile_km, ile_pali, cena_paliwa):
    koszt_paliwa = policz_koszt(ile_km, ile_pali, cena_paliwa)
    litry = policz_koszt(ile_km, ile_pali, cena_paliwa)
    out = f"""
    Na trasie:,
    koszt paliwa to {koszt_paliwa},
    auto spali {litry} litrow paliwa 
    """

dane = pobierz_dane()
koszt = policz_koszt(dane[2],dane[3],dane[4])
print(wydrukuj(*dane))
