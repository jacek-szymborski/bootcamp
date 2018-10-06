x = int(input("Pozycja x: "))
y = int(input("Pozycja y: "))
krawedz = int(100) #("Podaj dlugosc krawedzi planszy: ")
pozycja = "Żadna"

#lgr = x <= 0.1*krawedz and y >= 0.9*krawedz
#pgr = x >= 0.9*krawedz and y >= 0.9*krawedz
#ldr = x <= 0.1*krawedz and y <= 0.1*krawedz
#pdr = x >= 0.9*krawedz and y <= 0.1*krawedz

if x <= 0.1 * krawedz and y >= 0.9 * krawedz:
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
elif x < 0.1 * krawedz and y > 0.1 * krawedz and y < 0.9 * krawedz:
    pozycja = "gk"
