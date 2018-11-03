def test_Basket():
    basket = Basket()
    assert basket.produkty == []

def test_Product():
    pass

# def test_basket_add_product():
#     assert basket.add_product(product,5) ==


class Basket:

    def __init__(self):
        self.produkty = []

    def add_product(self):
        pass

    def count_total_price(self):
        pass

    def generate_report(self):
        pass


class Product:

    def __init__(self, id, name, unit_price):
        self.id = id
        self.name = name
        self.unit_price = unit_price