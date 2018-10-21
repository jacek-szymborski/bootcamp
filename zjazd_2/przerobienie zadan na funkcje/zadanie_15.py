from random import randint

sx = randint(1,10)
sy = randint(1,10)

gx = randint(1,10)
gy = randint(1,10)
lr_p = 0

while True:
    odleglosc_min = abs(sx - gx) + abs(sy - gy)
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

    lr = lr_p + 1
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

