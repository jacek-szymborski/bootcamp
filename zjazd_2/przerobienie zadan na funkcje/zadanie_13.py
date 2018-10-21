def pobierz_dane():
    ile_pomiarow = int(input("Podaj ilość pomiarów: "))
    temperatury = []
    for i in range(ile_pomiarow):
        temp = int(input(f"Podaj tempaeraturę z dnia {i+1}: "))
        temperatury.append(temp)
    return temperatury

def policz_srednia(temperatury):
    srednia = sum(temperatury) / len(temperatury)
    return srednia #alternatywnie: reutrn sum(temperatury) / len(temperatury)

def policz_minmax(temperatury):
    tmin_ = min(temperatury)
    tmax_ = max(temperatury)

    return tmin_, tmax_

def prezentuj_dane(srednia,tmin_, tmax):
    print(srednia)
    print(tmin_)
    print(tmax_)

dane = pobierz_dane()
srednia_temp = policz_srednia(dane)
tmin_, tmax_ = policz_minmax(dane)
prezentuj_dane(srednia_temp, tmin_, tmax_)