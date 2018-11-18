import csv

def przezycie_ogolne():
    with open('dane/titanic_train.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        przezyli = 0
        nie = 0
        wynik = []
        for row in data:
            if row[1] == '1':
                przezyli += 1
            if row[1] == '0':
                nie += 1
        wynik.append(przezyli)
        wynik.append(nie)
        # print(wynik)
        return wynik

# with open ('dane/titanic_train.csv') as csvfile:
#     data = csv.DictReader(csvfile, delimiter=",")
#     dlugosci = {}
#     for row in data:
#         dlugosci[row['Survived']] = dlugosci.get(row['Survived'], 0) + 1
#     przezylo = dlugosci['1']
#     zginelo = dlugosci['0']
#
#     print(f"Przezylo z ogolu {round(100*przezylo/(przezylo+zginelo), 2)}")
#     print(f"Zginelo z ogolu {round(100*zginelo/(przezylo+zginelo), 2)}")
#
# def srednia():
#
#     with open ('dane/titanic_train.csv') as csvfile:
#         data = csv.DictReader(csvfile, delimiter=",")
#
#         how_many_women = 0
#         sum_woman_age = 0
#
#         for row in data:
#
#             if row['Sex'] == 'female' and row['Age'] != "":
#                 how_many_women += 1
#                 sum_woman_age += float(row['Age'])
#
#         return sum_woman_age/how_many_women