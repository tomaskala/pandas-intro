import math
import pandas as pd
import matplotlib.pyplot as plt


iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


# ## 2. Scatterplot
# * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
# * Slouží k vizualizaci vztahu 2 numerických proměnných.
# * Pozor na nastavení velikosti obrázku -- obdélník může klamat.

iris.plot("sepal_width", "sepal_length", kind="scatter")
plt.show()

species_num = iris["species"].replace({"setosa": 1, "versicolor": 2, "virginica": 3})

iris.plot.scatter(
    "sepal_width",
    "sepal_length",
    c=species_num,
    s=50,
    colormap="viridis",
    sharex=False,  # Jinak se nezobrazí popisky osy x, protože graf a colormap napravo mají stejnou x-osu.
    figsize=(16, 10)
)
plt.show()
