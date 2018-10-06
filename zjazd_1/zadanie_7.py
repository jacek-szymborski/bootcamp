a = int(input("Liczba?: "))
podz_2 = a % 2 == 0
podz_3 = a % 3 == 0
w_10 = a > 10
siedem = a == 7

print(podz_2, podz_3, w_10, siedem)

wynik = (podz_2 and
         podz_3 and
         w_10) or a == 7

out = wynik
print(out)
