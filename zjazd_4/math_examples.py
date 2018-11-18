import math

class sphere:

    def __init__(self, r):
        self.promien = r

    def pole(self):
        pole = 4 * math.pi * self.promien ** 2
        return pole

    def objetosc(self):
        objetosc = (4/3) * math.pi * math.pow(self.promien, 3)
        return objetosc

s = (sphere(10))

print(s.objetosc())
print(s.pole())