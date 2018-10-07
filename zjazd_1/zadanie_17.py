lista = []
i = 1
iteracje = int(input("Wprowadz wielkosc listy:"))

print(lista,i)
while i <= iteracje:
    liczba = int(input("Wprowadz liczbe:"))
    lista.append(liczba)
    i += 1
    print(lista,i)

srednia = sum(lista)/iteracje
print(srednia)
