class ElectricCar:

    def __init__(self, max_range):
        self.max_range = max_range
        self.possible_distance = max_range

    def drive(self, distance):
        if distance >= self.possible_distance:
            can_travel = self.possible_distance
            self.possible_distance = 0

            return can_travel

        self.possible_distance -= distance

        return distance

    def charge(self):
        return 50


car = ElectricCar(100)
print(car.drive(70))
print(car.drive(50))
print(car.drive(50))

def test_ElectricCar():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.charge(50) == 50