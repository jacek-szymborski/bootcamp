import matplotlib.pyplot as plt
from csv_loader import przezycie_ogolne

sizes = przezycie_ogolne
labels = 'przezyli','nieprzezyli'

plt.pie(sizes, labels)

plt.show()