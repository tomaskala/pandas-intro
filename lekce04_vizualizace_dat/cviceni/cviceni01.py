import matplotlib.pyplot as plt
import pandas as pd


kostky = pd.read_csv("kostky.txt", header=None)[0]

# a.
kostky.hist(bins=11)
plt.show()

# Nejcasteji padla hodnota 7.
# Overeni:
print(kostky.value_counts())

# b.
# Ano.
