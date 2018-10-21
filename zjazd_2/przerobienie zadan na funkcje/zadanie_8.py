a = float(input("Podaj dlugosc opakowania [CM}: "))
b = float(input("Podaj szerokosc opakowania [CM}: "))
c = float(input("Podaj wysokosc opakowania [CM}: "))

objetosc = a * b * c

if objetosc > 1000:
    print("Objetosc tego opakowania to: ", objetosc/1000, "[L] i jest ona większa niż 1L")
else:
    print("Objetosc tego opakowania to:", objetosc/1000,"[L] i to jest za mało")
