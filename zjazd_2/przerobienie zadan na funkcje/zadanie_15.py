from random import randint

def losuj_wspolrzedne():
    x = randint(1,10)
    y = randint(1,10)
    return x,y

def minimalna_liczba_krokow():
    lr_przed = 0
    odleglosc_min = abs(sx - gx) + abs(sy - gy)

sx = losuj_wspolrzedne()
sy = losuj_wspolrzedne()
gx = losuj_wspolrzedne()
gy = losuj_wspolrzedne()

while True:
    ruch = input("Podaj ruch (WSAD): ")
    ruch = ruch.upper()

    if ruch == 'W':
            gy = gy + 1
    elif ruch == "S":
            gy = gy - 1
    elif ruch == "A":
            gx = gx - 1
    elif ruch == "D":
            gx = gx + 1
    if gx > 10 or gx < 1 or gy > 10 or gx < 1:
        print("Jestes poza plansza")
        break
    odleglosc_teraz = abs(sx - gx) + abs(sy - gy)

    lr = lr_przed + 1
    #restart jesli wykonal za duzo ruchow
    # if lr > 3:
    #     print ("Restart")
    #     sx = randint(1, 10)
    #     sy = randint(1, 10)
    #     gx = randint(1, 10)
    #     gy = randint(1, 10)


    if odleglosc_teraz < odleglosc_min:
        print (f"Cieplo skarb {sx},{sy}. Ty {gx},{gy}, {lr}")
    elif odleglosc_teraz > odleglosc_min:
        print (f"Zimno skarb {sx},{sy}. Ty {gx},{gy}, {lr}")
    if sx == gx and sy == gy:
        print("Wygrales!!!")
        break

