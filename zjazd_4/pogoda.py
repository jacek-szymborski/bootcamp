import json
import urllib.request

def get_input():
    lokalizacja = input("Podaj miasto: ")
    return lokalizacja

def get_woeid(lokalizacja):
    url_string = 'https://www.metaweather.com/api/location/search/?query=' + lokalizacja
    with urllib.request.urlopen(url_string) as f:
        dane = json.loads(f.read())
        woeid = dane[0]('woeid')
        print(dane)

def get_weather():
    pass

get_woeid(get_input())
get_weather()
