import pandas

mesta = pandas.read_csv("mesta.csv", index_col="mesto", encoding="utf-8")

# ## 2. Základní selekce

# Výběr hodnot v tabulce probíhá převážně pomocí "metody" `loc`.

# ### Výběr podle jmen řádků a sloupců

# #### 1. Pouze řádky

print(mesta.loc["brno"])

print(mesta.loc[["brno", "praha", "ostrava"]])

# V prvním případě jsme dostali výsledek orientovaný na výšku, ve druhém na šířku. Poprvé jsme chtěli údaj o 1 městu a dostali tzv. `Series`, podruhé jsme chtěli údaj o více městech a dostali `DataFrame` (podmnožinu toho původního DataFrame `mesta`).
#
# Mohli bychom si taky explicitně říct o výsledek pro 1 město v podobě DataFrame.

print(mesta.loc[["brno"]])

# Lze použít také rozsah (záleží samozřejmě na pořadí, v jakém máme data uložena).

print(mesta.loc["most":"praha"])

# Pozor na pořadí.

print(mesta.loc["praha":"most"])

print(mesta.loc["most":"praha":2])

print(mesta.loc[:"most"])

print(mesta.loc["most":])

# Kdy to dává a kdy naopak nedává smysl?

# #### 2. Pouze sloupce

print(mesta.loc[:, "kraj"])

print(mesta.loc[:, ["kraj", "linky"]])

# Zkrácený zápis.

print(mesta["kraj"])

print(mesta[["kraj", "linky"]])

# #### 3. Řádky a sloupce

print(mesta.loc["plzen", "linky"])

print(mesta.loc["most":"plzen", "obyvatel"])

print(mesta.loc[["most", "brno", "praha"], ["obyvatel", "vymera"]])

# ### Výběr podle pozic řádků a sloupců

# Pro připomenutí.

print(mesta)

print(mesta.iloc[2])

print(mesta.iloc[[2]])

print(mesta.iloc[2, 1:])

print(mesta.iloc[[2, 3, 5], [0, 1]])
