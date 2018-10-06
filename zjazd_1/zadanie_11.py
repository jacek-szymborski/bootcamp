krawedz = int(input("Podaj dlugosc krawedzi kwadratowej planszy: "))
x = int(input("Pozycja x: "))
y = int(input("Pozycja y: "))
pozycja = "Żadna"

#sprzawdzic wartosci graniczne

if x > krawedz or y > krawedz:
    print("poza planszą")
    raise ValueError("Za duża wartość!")
elif x <= 0.1 * krawedz and y >= 0.9 * krawedz:
    pozycja = "lgr"
elif x >= 0.9 * krawedz and y >= 0.9 * krawedz:
    pozycja = "pgr"
elif x <= 0.1 * krawedz and y <= 0.1 * krawedz:
    pozycja = "ldr"
elif x >= 0.9 * krawedz and y <= 0.1 * krawedz:
    pozycja = "pdr"
elif x < 0.1 * krawedz and y > 0.1 * krawedz and y < 0.9 * krawedz:
    pozycja = "lk"
elif x > 0.9 * krawedz and y > 0.1 * krawedz and y < 0.9 * krawedz:
    pozycja = "pk"
elif x > 0.1 * krawedz and x < 0.9 * krawedz and y > 0.9 * krawedz:
    pozycja = "gk"
elif x > 0.1 * krawedz and x < 0.9 * krawedz and y < 0.1 * krawedz:
    pozycja = "dk"
else:
    pozycja = "centrum"

print(pozycja)
