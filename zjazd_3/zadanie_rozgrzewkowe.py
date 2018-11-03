# Klasa pies ma metody: szczekanie - zuzywa jedna energie, spanie dodaje 2 energie.

class Dog:
    def __init__(self):
        self.energy = 10

    def bark(self):
        self.energy -= 1

    def sleep(self):
        self.energy += 2

    def get_energy(self):
        print(self.energy)

azor = Dog()
azor.bark()
azor.bark()
azor.bark()
azor.sleep()
azor.get_energy()