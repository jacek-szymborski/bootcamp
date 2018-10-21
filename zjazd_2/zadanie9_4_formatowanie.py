def test_formatuj():
    assert formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena = 10
    ) == "koszt 10 PLN\nkwota 10 brutto"

    assert formatuj(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto',
        'sumarycznie $cena'
    ) == "koszt 10 PLN\nkwota 10 brutto\nsumarycznie 10"


x = ("koszt $cena PLN","kwota $podatek brutto")
y = {"cena": 10, "podatek": 7}


def formatuj(*args,**kwargs):
    out = []
    for text in args:
        for klucz in kwargs:
            text = text.replace(f"${klucz}",str(kwargs[klucz]))
        out.append(text)
        print(text)
    return "\n".join(out)

formatuj(*x,**y)