lista_3 = []
lista_5 = []
lista_35 = []
lista_w = []

for liczba in range(0,101):
    lista_w.append(liczba)
    if liczba % 3 == 0 or liczba % 5 == 0:
        lista_35.append(liczba)
    if liczba % 3 == 0:
        lista_3.append(liczba)
    if liczba % 5 == 0:
        lista_5.append(liczba)

print(lista_w)
print(len(lista_3), len(lista_5), len(lista_35))
