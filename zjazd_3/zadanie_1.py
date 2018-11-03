class Produkt:

    def __init__(self, id, name, unit_price):
        self.id = id
        self.name = name
        self.unit_price = unit_price

    def print_info(self):
        print(f"Produkt = {self.name}, id: {self.id}, cena: {self.unit_price}")


product = Produkt(1,'Woda',10.99)
product.print_info()



