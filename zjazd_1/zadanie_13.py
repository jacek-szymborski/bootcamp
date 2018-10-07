ile_pomiarow = int(input("Podaj ilość pomiarów: "))
nr_pomiar = 1
suma_temp = 0

tmin_ = None
tmax_ = None

while nr_pomiar <= ile_pomiarow:
    temp = float(input(f"Podaj tempaeraturę z dnia {nr_pomiar}: "))
    suma_temp += temp #suma_temp = suma_temp + temp
    if nr_pomiar == 1:
       tmin_ = temp
       tmax_ = temp
    else:
        if temp > tmax_:
            tmax_ = temp
        if temp < tmin_:
            tmin_ = temp
    nr_pomiar += 1 # nr_pomiar = nr_pomiar + 1

srednia_temp = suma_temp / ile_pomiarow

print(srednia_temp)
print(tmin_, tmax_)
