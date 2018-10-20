# wprowadzanie liczb
zbior_liczb = set()
zbior_parz0100 = set(range(2,101,2))
user_input = None

while True:
    user_input = input("Wprowadz liczbe lub komende k: ")
    if user_input == "k":
        break
    liczba = int(user_input)
    zbior_liczb.add(liczba)
    print(zbior_liczb)
    ile = len(zbior_liczb & zbior_parz0100)
print(ile)



# policzyc liczby parzyste