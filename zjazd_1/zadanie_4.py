cena_kg = 10
waga = float(input("Ile zważyć szanowna Pani? "))
naleznosc = cena_kg * waga

out = f"""

Cena: {cena_kg} PLN/KG
Waga: {waga} KG
Należnośc wynosi: {naleznosc} PLN
"""

print(out)