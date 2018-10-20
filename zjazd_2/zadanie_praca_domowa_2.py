#zliczanie anków między nawiasami <>
nawias1 = 0
nawias2 = 0
my_text = input("Podaj: ")

for index, i in enumerate(my_text):
    if i == "<":
        nawias1 = index
    if i == ">":
        nawias2 = index

print(nawias2 - nawias1 - 1)