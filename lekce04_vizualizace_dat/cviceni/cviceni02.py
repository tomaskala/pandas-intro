import matplotlib.pyplot as plt
import pandas as pd


casy = pd.read_csv("callcentrum.txt", header=None)[0]

casy_split = casy.str.split(":", expand=True)
casy_split[0] = pd.to_numeric(casy_split[0])
casy_split[1] = pd.to_numeric(casy_split[1])

casy_sekundy = casy_split[0] * 60 + casy_split[1]

casy_sekundy.hist()
plt.show()

casy_sekundy.plot(kind="box")
plt.show()

# lol nevim co jde vycist, asi ze cim vyssi cas, tim nizsi cetnost
# formalne lze rict, ze se casy ridi exponencialnim rozdelenim (https://en.wikipedia.org/wiki/Exponential_distribution)
