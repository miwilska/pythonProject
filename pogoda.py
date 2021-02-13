import requests
import pandas as pd
import matplotlib.pyplot as plt


res = requests.get("http://api.gios.gov.pl/pjp-api/rest/data/getData/4079")
res = res.json()
lomza = pd.DataFrame( res['values'])
lomza['miasto'] = 'Łomża'


res = requests.get("http://api.gios.gov.pl/pjp-api/rest/data/getData/3195")
res = res.json()
zakopane = pd.DataFrame( res['values'])
zakopane['miasto'] = 'Zakopane'


res = requests.get("http://api.gios.gov.pl/pjp-api/rest/data/getData/4681")
res = res.json()
gdansk = pd.DataFrame( res['values'])
gdansk['miasto'] = 'Gdańsk'

res = requests.get("http://api.gios.gov.pl/pjp-api/rest/data/getData/3584")
res = res.json()
warszawa1 = pd.DataFrame( res['values'])
warszawa1['miasto'] = 'Warszawa 1'

df = pd.concat([lomza, zakopane, gdansk, warszawa1])
df.dropna()
df = df.sort_values('date')


df_p  = df.pivot(index='date', columns='miasto', values='value')
df_p.index.name = None

print(df_p)
g = df_p.plot(figsize=(15, 4), title='Poziom PM10')
g.axhline(y=20, color='red')
plt.show()