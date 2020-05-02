import pandas

df = pandas.read_csv("jmena100.csv", index_col="jméno", encoding="utf-8")

print(df.head())
print()

# a.
print(df.loc["Martin"])
print()

# b.
print(df.loc[["Martin", "Zuzana", "Josef"]])
print()

# c.
print(df.loc[:"Martin"])
print()

# d.
print(df.loc["Martin":"Tereza", "věk"])
print()

# e.
print(df.loc["Libor":, ["věk", "původ"]])
print()

# f.
print(df.loc[:, "věk":"původ"])
