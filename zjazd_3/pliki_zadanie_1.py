import sys

nazwa_pliku = sys.argv[1]

with open(nazwa_pliku) as f:
    i = 1
    for line in f:
        print(str(i) + "." + ' ' + line)
        i += 1