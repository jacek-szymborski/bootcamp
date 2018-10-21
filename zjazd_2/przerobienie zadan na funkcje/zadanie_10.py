l1 = int(input("Podaj pierwszą liczbę: "))
l2 = int(input("Podaj drugą liczbę: "))
dzialanie = str(input("Wybierz działanie (+,-,*,/): "))

if dzialanie == "+":
    wynik = l1 + l2
    print(wynik)
elif dzialanie == "-":
    wynik = l1 - l2
    print(wynik)
elif dzialanie == "*":
    wynik = l1 * l2
    print(wynik)
elif dzialanie == "/" and l2 != 0:
    wynik = l1 / l2
    print(wynik)
elif dzialanie == "/" and l2 == 0:
    print("Nie można dzielić przez zero")
#    pass
else:
    print("Wybrałeś nieobsługiwane działanie")
    raise valueerror ("Wybrałeś nieobsługiwane działanie")
