r = range(10)
for x in r:
    print(f"{x:3}",end='')
print()
print()
for x in r:
        print(x, end='')
        for y in r:
            print(f"{x*y:3}",end='')
        print()