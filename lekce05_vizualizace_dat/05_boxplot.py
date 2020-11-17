import math
import pandas as pd
import matplotlib.pyplot as plt


iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


# ## 5. Boxplot
# * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html
# * Slouží k vizualizaci vztahu kategorické a numerické proměnné.
# * Boxplot zobrazí pro každý druh kosatce krabici.
#     * Vodorovná čára uvnitř krabice je medián.
#     * Spodní a horní meze krabice jsou 25% a 75% kvartily.
#     * Označíme IQR (interquartile range, mezikvartilové rozpětí) jako rozdíl 75% a 25% kvartilu.
#     * Tykadla nad a pod krabicí jsou (obvykle) 1.5-násobek IQR.
#     * Všechny body mimo tykadla jsou označené tečkou a chápeme je jako odlehlá pozorování (anomálie?).

iris.boxplot("petal_length", by="species", figsize=(16, 10))
plt.show()

iris.boxplot(by="species", figsize=(16, 10))
plt.show()
