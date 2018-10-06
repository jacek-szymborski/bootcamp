liczba = float(input("Podaj liczbę: "))

czy_wieksza = liczba > 10
czy_mniejsza_rowna = liczba <= 15
czy_podzielna_2 = (liczba % 2) == 0

out = f"""
Twoja iczba to: {liczba}
Czy jest większa od 10? : {czy_wieksza}
Czy jest mniejsza lub równa 15? : {czy_mniejsza_rowna}
Czy jest podzielna przez 2? : {czy_podzielna_2}
"""

print(out)
