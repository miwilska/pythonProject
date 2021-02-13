'''
Biblioteka requests - standardowa biblioteka do zapytań HTTP

Biblioteka requests, nie jest jednyną, jednak jest najczęściej stosowaną biblioteką do tworzenia zapytań HTTP. 
Tym samym jest często stosowana przy web scrapingu oraz komunikacji z REST API.
'''
import requests

req = requests.get("https://analityk.edu.pl")

# Status_code, informuje nasz czy operacja się powiodła. Wartość 200, znaczy że tak.
# Przykładowo wartość 404, będzie oznaczać, że nie ma takiej strony.
print(req.status_code)

# Następnie możemy, w łatwy sposób, wyświetlić zwrócony nagłówek, lub treść
print(req.headers)


szukaneSłowo = 'computer'
res = requests.get('https://www.dictionary.com/browse/' + szukaneSłowo)
print(res.url)
#print(res.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
desc = soup.find_all("meta")
for tag in soup.find_all("meta"):
    if tag.get("name") == "description":
        print(tag.get("content"))

parameters = { 'masto' : 'Warszawa', 'państwo' : 'Polska' }
r = requests.get('https://httpbin.org/get', params=parameters)
#print(r.text)

res = requests.get('https://api.github.com/user', auth=('login', 'haslo'))
print(res.text)

