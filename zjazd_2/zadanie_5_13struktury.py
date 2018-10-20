#zadanie 13 struktury danych

lista = [x/10 for x in range(0,11)]
print(lista)

zbior_tupli = {(x,x**2,x**3) for x in range(0,11)}
print(zbior_tupli)

zbior_nap = {"abc","koza","ala ma kota"}
slownik_map = {x:len(x) for x in zbior_nap}
print(slownik_map)



