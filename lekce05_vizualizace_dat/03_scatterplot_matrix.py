import math
import pandas as pd
import matplotlib.pyplot as plt


iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


# ## 3. Scatterplot matrix
# * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.plotting.scatter_matrix.html
# * Máme-li proměnných víc, můžeme je všechny zakreslit do tzv. scatterplot matrix.
# * Na diagonále jsou histogramy jednotlivých proměnných, mimo diagonálu scatterploty mezi každou dvojicí proměnných.
# * Je dobré si něco takového vykreslit na začátku analýzy, kdy se teprve snažíme udělat obrázek o tom jaké proměnné vlastně máme.

pd.plotting.scatter_matrix(iris, figsize=(10, 10))
plt.show()

# Alternativně si můžeme místo histogramů nechat vykreslit odhady hustoty pravděpodobnosti -- vyhlazené histogramy.

pd.plotting.scatter_matrix(iris, diagonal="kde", figsize=(10, 10))
plt.show()
