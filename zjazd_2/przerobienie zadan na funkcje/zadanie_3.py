def test_prez_osobe():
    assert prez_osobe("Jacek",172) == """"
    Imi
    
    """

def prez_osobe(imie,wzrost):


output_n = f"Imie: {imie} \nWzrost: {wzrost}"

print(output_n)


output_c = f"""
Imię: {imie}
Wzrost: {wzrost}
"""

print(output_c)

