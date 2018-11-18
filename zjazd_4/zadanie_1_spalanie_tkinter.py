import tkinter
import numpy as np

def obliczanie():
    spalanie = np.float64(spalanie_entry.get())
    dystans = np.float64(dys_entry.get())
    cena = np.float64(cena_entry.get())
    policzone = float((spalanie/100)*dystans*cena)
    wynik.configure(text=policzone)


root = tkinter.Tk()

spalanie_entry = tkinter.Entry(master=root)
spalanie_label = tkinter.Label(master=root, text = 'Ile pali na 100?')

spalanie_label.pack()
spalanie_entry.pack()

dys_entry = tkinter.Entry(master=root)
dys_label = tkinter.Label(master=root, text = 'Dystans do przejechania?')

dys_label.pack()
dys_entry.pack()

cena_entry = tkinter.Entry(master=root)
cena_label = tkinter.Label(master=root, text = 'Cena 1L paliwa?')

cena_label.pack()
cena_entry.pack()


wynik_label_opis = tkinter.Label(master=root, text = 'Wynik')
wynik_label_opis.pack()

wynik = tkinter.Label(master=root, text = '-')
wynik.pack()

button = tkinter.Button(master=root, text = 'Policz', command=obliczanie)
button.pack()
root.title('Kalkulator kosztów przejazdu')
root.mainloop()

