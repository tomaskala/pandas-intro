import math
import pandas as pd
import matplotlib.pyplot as plt

# Budeme pracovat s [iris](https://archive.ics.uci.edu/ml/datasets/Iris/) datasetem. Jde o velmi často využívaný dataset obsahující údaje o okvětních lístcích 3 druhů kosatců (*setosa*, *versicolor*, *virginica*). Data sesbíral v roce 1936 slavný statistik R. A. Fisher.
# <img src="iris.jpg" width=400/>

# Data netřeba stahovat, pandy je stáhnou přímo z internetu.

iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print(iris.head())

# O každém druhu kosatce máme 50 měření.

print(iris["species"].value_counts())

# ## Kategorická vs. numerická data

# Vhodný způsob vizualizace vybíráme podle typu dat.
#
# **Kategorická data**
# * Ekvivalentně diskrétní, nominální.
# * Nabývají konečně mnoha hodnot.
# * Nedává smysl mezi sebou porovnávat hodnoty, sčítat je, ...
# * Příklady: barva, rostlinný druh, telefonní číslo, adresa, typ podaného léku, ...
#
# **Numerická data**
# * Ekvivalentně spojitá, číselná.
# * Mohou nabývat konečně i (formálně) nekonečně mnoha hodnot.
# * Dává smysl mezi sebou porovnávat hodnoty a provádět s nimi matematické operace.
# * Příklady: věk, výška, výše úvěru, počet připojení na server, ...

# ## 1. Histogram
# * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html
# * Vizualizace četností v jednotlivých přihrádkách.
# * Pozor na vhodnou volbu počtu přihrádek.

# Histogramy jednotlivých numerických proměnných.

iris.hist(figsize=(16, 10))
plt.show()

# Barevně odlišíme podle typu kosatce.

fig = plt.figure(figsize=(16, 10))
iris.loc[iris["species"] == "setosa", "sepal_width"].hist(label="setosa")
iris.loc[iris["species"] == "versicolor", "sepal_width"].hist(label="versicolor")
iris.loc[iris["species"] == "virginica", "sepal_width"].hist(label="virginica")
plt.legend()
plt.show()

iris["sepal_width"].hist(bins=20, figsize=(16, 10))
plt.show()
