import math
import pandas as pd
import matplotlib.pyplot as plt


iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


# ## 6. Časové řady
# * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
# * Poslední co si ukážeme je jak vykreslit časovou řadu. Pokud má Series index typu datetime, chápou ji pandy jako časovou řadu. Při vykreslení tedy x-osu anotují datumy.

# Z kodim.cz ukradneme data o pohybech na účtu.

pohyby = [746, 52, -749, -63, 71, 958, 157, -1223, -1509, -285, -350, 728, -260, 809, -164, 243, -238, 233, -646, -82, -275, 179, 417, 149, 301, 957, -711, 376, 421, -15, -663]

import datetime as dt
data = [dt.date(2019, 3, d) for d in range(1, 32)]
ucet = pd.Series(pohyby, index=data)
print(ucet.head())

ucet.plot(figsize=(16, 10))
plt.show()

# Pomocí kumulativní sumy spočítáme aktuální zůstatek na účtu.

ucet.cumsum().plot(figsize=(16, 10))
plt.show()

# Můžeme vykreslit barplot.

ucet.cumsum().plot(kind="bar", grid=True, figsize=(16, 10))
plt.show()
