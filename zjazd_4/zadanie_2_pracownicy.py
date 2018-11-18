import json

def dodaj_pracownika():
    lista_prac = []
    pracownik = {}
    print(f"Dodawanie pracownika:\n")
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok = input("Rok urodzenia: ")
    pensja = input("Pensja: ")
    pracownik = {"imie":imie,"nazwisko":nazwisko,"rok":rok,"pensja":pensja}
    lista_prac.append(pracownik)
    with open("dane.json", "w") as f:
        json.dump(lista_prac, f)

def wypisz():
    for pracownik in lista_prac

tryb = input("Co chcesz zrobić? [d - dodaj, w - wypisz]")

if tryb == "d":
    dodaj_pracownika()

elif tryb == "w":
        pass
else:
    Break

