import datetime

rok_ur = int(input("Podaj rok urodzenia: "))
now = datetime.datetime.now()
akt_rok = now.year

if akt_rok - rok_ur >= 18:
    print("Stary")
else:
    print("Młody")

