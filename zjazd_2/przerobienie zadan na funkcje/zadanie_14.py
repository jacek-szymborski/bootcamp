lmin = None
lmax = None

while True:
    dane_wejsciowe = input(f"Podaj liczbe lub wpisz X: ")
    if dane_wejsciowe == "X":
        break
    liczba = int(dane_wejsciowe)
#ustawnie lmin albo lmax w  zależności od tego jaką wartość ma liczba
    if lmin is None or liczba < lmin:
        lmin = liczba
    if lmax is None or liczba > lmax:
        lmax = liczba

if not lmax or not lmin: #jeśli nie jest ustawiona żadna wartość lmin albo lmax, jeśli jest none to pętla dostaje false
    print("brak danych")
else:
    print(lmin)
    print(lmax)
