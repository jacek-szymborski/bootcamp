import tkinter

def sumuj():
    a = float(a_entry.get())
    b = float(b_entry.get())
    wynik.configure(text=a+b)


root = tkinter.Tk()

a_entry = tkinter.Entry(master=root)
a_label = tkinter.Label(master=root, text = 'Paramter a')

a_label.pack()
a_entry.pack()

b_entry = tkinter.Entry(master=root)
b_label = tkinter.Label(master=root, text = 'Paramter b')

b_label.pack()
b_entry.pack()

wynik_label_opis = tkinter.Label(master=root, text = 'Wynik')
wynik_label_opis.pack()

wynik = tkinter.Label(master=root, text = '-')
wynik.pack()

button = tkinter.Button(master=root, text = 'Policz', command=sumuj)
button.pack()
root.title('Sumator')
root.mainloop()

