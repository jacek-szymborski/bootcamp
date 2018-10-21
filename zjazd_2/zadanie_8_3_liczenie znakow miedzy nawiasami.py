def test_policz_znaki_domyslne():
    assert policz_znaki("ala ma <kota> a kot ma ale") == 4
def test_policz_znaki_kwadratowe():
    assert policz_znaki("ala [kota [a kot]] ma [ale]", "[", "]") == 18
def test_policz_znaki_domyslne_zagnizdzone():
    assert policz_znaki("a <a<a<a>>>") == 6
def test_policz_znaki_poziom_zagl_0():
    assert policz_znaki("aaa") == 0
def test_policz_znaki_poziom_zagl_1():
    assert policz_znaki("a<aa") == 1
def test_policz_znaki_poziom_zagl_2():
    assert policz_znaki("a<<aa") == 2
def test_policz_znaki_poziom_zagl_minus1():
    assert policz_znaki("a<<aa>") == 1

def policz_znaki(napis, start="<", stop=">"):
    poziom_zaglebienia = 0
    wynik = 0
    #sprawdzenie poziomu zaglebienia
    for znak in napis:
        if znak == start:
           poziom_zaglebienia += 1
        elif znak == stop:
           poziom_zaglebienia -= 1
        else:
            wynik += poziom_zaglebienia
    return wynik

print(policz_znaki("ala [kota [a kot]] ma [ale]", "[", "]"))
