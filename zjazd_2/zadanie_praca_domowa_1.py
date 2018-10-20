napis = input("Podaj napis: <")
samo = 0
SAMOGLOSKI = 'aeiou'

for znak in napis:
    if znak in SAMOGLOSKI:
        samo += 1

print(f"W wyrazie {napis} jest {samo} samoglosek")
