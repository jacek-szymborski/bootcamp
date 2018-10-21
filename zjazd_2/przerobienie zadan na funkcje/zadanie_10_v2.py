#zagnieżdzony if
#rzucenie wyjątkiem

def pobierz_dane():
    l1 = int(input("Podaj pierwszą liczbę: "))
    l2 = int(input("Podaj drugą liczbę: "))
    dzialanie = str(input("Wybierz działanie (+,-,*,/): "))
    return l1,l2,dzialanie

def licz(l1,l2,dzialanie):
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

def wynik():
    dane = pobierz_dane()
    wynik = licz(*dane)

wynik()

