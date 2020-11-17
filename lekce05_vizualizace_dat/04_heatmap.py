import math
import pandas as pd
import matplotlib.pyplot as plt


iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


# ## 4. Heatmap - korelační matice
# * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html
# * https://seaborn.pydata.org/generated/seaborn.heatmap.html
# * Další způsob vizualizace vztahu mezi páry numerických proměnných.
# * Dává podobnou informaci jako scatterplot matrix, ale kvantifikovanou.
# * Pomocí `iris.corr()` napočítáme korelační matici -- tabulku, která má v každé buňce korelaci mezi 2 proměnnými.
# * Následně ji vizualizujeme a jednotlivé buňky obarvíme podle korelace. Čím světlejší, tím vyšší korelace.

import seaborn as sns

corr = iris.corr()
print(corr)

fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(corr, annot=True, ax=ax)
plt.show()
