import pandas

mesta = pandas.read_csv("mesta.csv", index_col="mesto", encoding="utf-8")

# ## 4. Index

# Pokud index explicitně nevytvoříme jako v příkladu předtím, Pandas ho vytvoří automaticky číselný. Je to podobné jako číslování řádků v Excelu, každá tabulka má index. Jde jen o to, že si ho můžeme pojmenovat sami, máme-li k tomu rozumný důvod.

# Připomenutí: takhle vypadal náš DataFrame doteď.

print(mesta)

# Nespecifikujeme explicitní index.

mesta = pandas.read_csv("mesta.csv", encoding="utf-8")
print(mesta)

# Index je teď číselný. Přístup pomocí názvu řádků (`loc`) nebo pomocí jejich čísel (`iloc`) je teď velmi podobný. Jediný rozdíl je v indexování rozsahem.

print(mesta.loc[:4])

print(mesta.iloc[:4])

# Index můžeme manuálně nastavit na jeden ze sloupců. Ten potom zmizí z datové části, a přesune se do pozice indexu.

print(mesta.set_index("mesto"))
