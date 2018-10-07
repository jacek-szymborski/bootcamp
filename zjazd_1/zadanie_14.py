lmin = None
lmax = None

while True:
    dane_wejsciowe = input(f"Podaj liczbe lub wpisz X: ")
    if dane_wejsciowe == "X":
        break
    liczba = int(dane_wejsciowe)

    if lmin is None or liczba < lmin:
        lmin = liczba
    if lmax is None or liczba > lmax:
        lmax = liczba

if not lmax or not lmin:
    print("brak danych")
else:
    print(lmin)
    print(lmax)
