import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A?format=JSON") as f:
    kursy = json.loads(f.read())
    print(kursy)

rates = kursy[0]['rates']
# for r in rates:
#     print(f"- {r['code']} - {r['mid']}")

waluta = input('Podaj walute, ktora kupujesz: ')
ile = float(input('ile?: '))

for r in rates:
    if r['code'] == waluta:
        result = ile * r['mid']

print("płacisz",result)