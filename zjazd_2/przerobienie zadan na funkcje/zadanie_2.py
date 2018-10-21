def test_policz_pole():
    assert pole_trapezu(3,9,6.5) == 39.0

def pole_trapezu(a,b,h):
    pole = ((a + b) * h) / 2
    return pole

#assert pole == 40 #nadaje sie do testów
#print(f"pole trapezu {a} i {b} oraz {h} wynosi {pole}")
