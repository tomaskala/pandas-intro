# ## 1. Základní práce s DataFrame

# ### Načítání dat

# * Pandas umí načítat všechny možné formáty -- CSV, JSON, Excel, HTML, SQL databáze, a spoustu dalších, stejně tak je možné do nich ukládat.
#     * Toho lze využít např. pro převod dat z Excelu do CSV.
# * Rovněž umožňují stáhnout data z internetu -- místo cesty k souboru na disku dáme URL adresu.
# * Podporují kompresi -- ZIP archivy a podobně.

import pandas

# Příklad: tabulka měst provozujících tramvajovou dopravu.

mesta = pandas.read_csv("mesta.csv", index_col="mesto", encoding="utf-8")
print(mesta)

# ### Základní informace o tabulce

# Datové typy, názvy sloupců, počet neprázdných hodnot.

print(mesta.info())

# Velikost.

print(mesta.shape)

# Názvy sloupců.

print(mesta.columns)

print(list(mesta))

# Základní statistické údaje -- jen na číselných sloupcích.

print(mesta.describe())

# Prvních pár řádků tabulky.

print(mesta.head())
