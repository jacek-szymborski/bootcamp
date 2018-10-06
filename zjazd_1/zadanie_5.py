miasto_z = input("Skąd jedziesz?: ")
miasto_do = input("Dokąd?: ")
ile_km = float(input("Ile to km?: "))
trasa = f"{miasto_z} - {miasto_do}"
ile_pali = float(input("Ile spala Twój samochód na 100km?: "))
cena_paliwa = float(input("Ile kosztuje litr paliwa?: "))

koszt_paliwa = cena_paliwa * ile_pali * (ile_km / 100)
litry = ile_km / 100 * ile_pali

out = f"""
Na trasie: {trasa},
koszt paliwa to {koszt_paliwa},
auto spali {litry} litrow paliwa 
"""

print(out)
