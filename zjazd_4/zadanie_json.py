import json

# tworzenie obiektu ythonowego

meble = ["krzesło", "szafa", "komoda"]

print(type(meble))

meble_as_json = json.dumps(meble)
print(meble_as_json)
print(type(meble_as_json))

odczytane_z_json = json.loads(meble_as_json)
print(odczytane_z_json)
print(type(odczytane_z_json))

with open("meble.json",'w') as f:
    json.dump(meble, f)


with open("meble.json") as f:
    json.load(f)
    print(meble)
