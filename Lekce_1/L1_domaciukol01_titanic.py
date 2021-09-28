import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

titanic = pandas.read_csv("titanic.csv")

import numpy
titanic_pivot = pandas.pivot_table(titanic, index = "Sex", columns = "Pclass", values = "Survived", aggfunc=numpy.sum)
print(titanic_pivot)
