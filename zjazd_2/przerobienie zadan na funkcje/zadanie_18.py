lista = [-1, 2, -3, 4, -5, 6, -7, 8, -9, -12, -1212,0,0]
lista_u = []
lista_d = []
lista_z = []

for liczba in lista:
    if liczba < 0:
        lista_u.append(liczba)
    elif liczba > 0:
        lista_d.append(liczba)
    elif liczba == 0:
        lista_z.append(liczba)

count_d = len(lista_d)
count_u = len(lista_u)
count_z = len(lista_z)
print(f"Dodatnich jest {count_d}, a ujemnych {count_u}. Bylo tez {count_z} zer.")
