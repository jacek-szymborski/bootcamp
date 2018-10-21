def kalkulator(a, b, operacja="+"):
    if operacja == "+":
        return a+b
    elif operacja == "-":
        return a-b

print(kalkulator(1, 2))
print(kalkulator(1, 2, "-"))
