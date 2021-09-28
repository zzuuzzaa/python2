import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)
pujcovna_kol = pandas.read_csv("london_merged.csv")

pujcovna_kol["timestamp"] = pandas.to_datetime(pujcovna_kol["timestamp"])
pujcovna_kol["year"] = pujcovna_kol["timestamp"].dt.year

import numpy
porovnani_pocasi_pivot = pandas.pivot_table(pujcovna_kol, index = "year", columns = "weather_code", values = "cnt", aggfunc=numpy.count_nonzero)

print(porovnani_pocasi_pivot.head())
