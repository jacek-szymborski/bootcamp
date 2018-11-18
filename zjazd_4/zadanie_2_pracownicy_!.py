import json

try:
    with open("pracownicy.json") as f:
        pracownicy = json.load(f)

except FileNotFoundError:
    pracownicy = []

action = input("Co chcesz zrobić? [d - dodaj, w - wypisz]")

if action == "d":
    print(f"Dodawanie pracownika:\n")
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))
    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok": rok,
        "pensja": pensja
    }
    pracownicy.append(pracownik)
    with open("pracownicy.json", "w") as f:
        json.dump(pracownicy, f)

elif action == "w":
        for i,pracownik in enumerate(pracownicy, start=1):
            print(f"- [{i}] {pracownik['imie']} {pracownik['nazwisko']}")
else:
    Break