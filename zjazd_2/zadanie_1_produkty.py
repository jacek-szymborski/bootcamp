# print("lista:")
# for produkt in produkty.items():
#     name, cena = produkt
#     print(name, cena)
#
# produkt_wybrany = input("Co chcesz kupic? ")
# ile = float(input("ïle?"))
# cena = produkty[produkt_wybrany]
#
# koszt = ile * cena
# print(koszt)

produkty = {"ziemniaki":2,"bataty":3,"pomidory":6}
magazyn = {"ziemniaki":10,"bataty":10,"pomidory":10}

do_zaplaty = 0
while True:
    print("lista:")
    for produkt in produkty:
        print(produkt,produkty[produkt])
    komenda = input("Co chcesz zrobic? [k}upic, [z]akonczyc [d]odac")
    if komenda == "z":
        break
    elif komenda == "k":
        produkt_wybrany = input("Co chcesz kupic? ")
        if produkt_wybrany not in produkty:
            print("Nie mamy w sklepie")
            continue
        ile = float(input("ïle?"))
        if (magazyn[produkt_wybrany] - ile) <= 0:
            print("Brak w magazynie")
            continue
        cena = produkty[produkt_wybrany]
        magazyn[produkt_wybrany] = magazyn[produkt_wybrany] - ile
        koszt = ile * cena
        do_zaplaty += koszt
    elif komenda == "d":
        produkt_do_dodania = input("Jaki produkt chcesz dodac? ")
        if produkt_do_dodania not in magazyn:
            magazyn[produkt_do_dodania] = 0
            cena_nowego = float(input("Podaj cene nowego:"))
            waga_dodawanie = float(input("Ïle dodajemy?"))
            produkty[produkt_do_dodania] = cena_nowego
            magazyn[produkt_do_dodania] = waga_dodawanie






print(magazyn)
print(do_zaplaty)
