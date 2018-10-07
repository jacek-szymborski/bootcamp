liczby = [5,2,1,4,3]
imax = None
imin = None
indeksy = list(range(len(liczby)))

for i in indeksy:
    if imax is None or liczby[i] > liczby[imax]:
        imax = i
    if imin is None or liczby[i] < liczby[imin]:
        imin = i

if imin is not None and imax is not None:
    temp = liczby[imin]
    liczby[imin] = liczby[imax]
    liczby[imax] = temp

print(liczby)

assert liczby == [1,2,5,4,3]

