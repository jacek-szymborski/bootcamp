def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0) == set()

def test_wecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaaaabbbccd",2) == {"a","b"}

napis = "aaaaabbbccd"

def wiecej_niz(napis, prog):
    licznik_liter = {}
    licznik_wiekszych = set()
    for litera in napis:
        if napis.count(litera) > prog:
            licznik_wiekszych.add

print(wiecej_niz(napis,2 ))
