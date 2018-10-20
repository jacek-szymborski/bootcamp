import pytest

def test_czy_pierwsza_dla_pierwszej():
    assert czy_jest_pierwsza(17)
    assert czy_jest_pierwsza(7)

def test_czy_pierwsza_dla_niepierwszej():
    assert not czy_jest_pierwsza(4)
    assert not czy_jest_pierwsza(9)

def czy_jest_pierwsza(liczba):
    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            return False
    return True

print(czy_jest_pierwsza(9))