#zagnieżdzony if
#rzucenie wyjątkiem


l1 = int(input("Podaj pierwszą liczbę: "))
l2 = int(input("Podaj drugą liczbę: "))
dzialanie = str(input("Wybierz działanie (+,-,*,/): "))

wynik = str("Wynik nieustalony")

if dzialanie == "+":
    wynik = l1 + l2
elif dzialanie == "-":
    wynik = l1 - l2
elif dzialanie == "*":
    wynik = l1 * l2
elif dzialanie == "/":
    if l2 == 0:
        raise ValueError ("Nie dziel przez zero")
    wynik = l1 / l2
else:
    raise ValueError ("Wybrałeś nieobsługiwane działanie")
print(wynik)