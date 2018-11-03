class Animal:

    def __init__(self, gatunek):
        self.gatunek = gatunek

azor = Animal("Canis Familiaris")
rudolf = Animal("Renifer")

print(azor.gatunek)
print(rudolf.gatunek)