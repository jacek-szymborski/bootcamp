from requests import get
from bs4 import beautifulsoup

url = 'https://helion.pl/search?qa=&serwisyall=&szukaj=python&wprzyg=&wsprzed=&wyczerp='

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

print(response.text)