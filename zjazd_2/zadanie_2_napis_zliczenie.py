napis = input("Podaj napis:")

#w podanym napisie liczy wystapienia poszczeglnych liter

liczniki_liter = {}

for litera in napis:
    # if litera not in liczniki_liter:
    #     liczniki_liter[litera] = 1
    # elif litera in liczniki_liter:
    #     liczniki_liter[litera] += 1
# to zamiast ifa
    liczniki_liter[litera] = liczniki_liter.get(litera,0) + 1

for litera in liczniki_liter:
    print(f"{litera} wystapila {liczniki_liter[litera]} razy")
