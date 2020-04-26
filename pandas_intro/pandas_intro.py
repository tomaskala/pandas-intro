# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Úvod do Pandas

# Potřeba nainstalovat jako modul do Pythonu. Pokud ještě nemáte, do terminálu (ne do Pythonovské konzole) napište:
# * na Windows `pip install pandas`,
# * na Linuxu nebo Macu `pip3 install pandas`.

# Pandas:
# * Je základní knihovna pro práci s daty v Pythonu.
# * Velká část datové analýzy obnáší právě práci s Pandas.
# * Datový soubor reprezentuje podobně jako tabulka v databázích, "DataFrame".

# ## 1. Základní práce s DataFrame

# ### Načítání dat

# * Pandas umí načítat všechny možné formáty -- CSV, JSON, Excel, HTML, SQL databáze, a spoustu dalších, stejně tak je možné do nich ukládat.
#     * Toho lze využít např. pro převod dat z Excelu do CSV.
# * Rovněž umožňují stáhnout data z internetu -- místo cesty k souboru na disku dáme URL adresu.
# * Podporují kompresi -- ZIP archivy a podobně.

import pandas

# Příklad: tabulka měst provozujících tramvajovou dopravu.

mesta = pandas.read_csv("mesta.csv", index_col="mesto", encoding="utf-8")
mesta

# ### Základní informace o tabulce

# Datové typy, názvy sloupců, počet neprázdných hodnot.

mesta.info()

# Velikost.

mesta.shape

# Názvy sloupců.

mesta.columns

list(mesta)

# Základní statistické údaje -- jen na číselných sloupcích.

mesta.describe()

# Prvních pár řádků tabulky.

mesta.head()

# ## 2. Základní selekce

# ![DataFrame](dataframe.svg)

# ### Výběr podle jmen řádků a sloupců

# #### 1. Pouze řádky

mesta.loc["brno"]

mesta.loc[["brno", "praha", "ostrava"]]

# V prvním případě jsme dostali výsledek orientovaný na výšku, ve druhém na šířku. Poprvé jsme chtěli údaj o 1 městu a dostali tzv. `Series`, podruhé jsme chtěli údaj o více městech a dostali `DataFrame` (podmnožinu toho původního DataFrame `mesta`).
#
# Mohli bychom si taky explicitně říct o výsledek pro 1 město v podobě DataFrame.

mesta.loc[["brno"]]

# Lze použít také rozsah (záleží samozřejmě na pořadí, v jakém máme data uložena).

mesta.loc["most":"praha"]

# Pozor na pořadí.

mesta.loc["praha":"most"]

mesta.loc["most":"praha":2]

mesta.loc[:"most"]

mesta.loc["most":]

# Kdy to dává a kdy naopak nedává smysl?

# #### 2. Pouze sloupce

mesta.loc[:, "kraj"]

mesta.loc[:, ["kraj", "linky"]]

# Zkrácený zápis.

mesta["kraj"]

mesta[["kraj", "linky"]]

# #### 3. Řádky a sloupce

mesta.loc["plzen", "linky"]

mesta.loc["most":"plzen", "obyvatel"]

mesta.loc[["most", "brno", "praha"], ["obyvatel", "vymera"]]

# ### Výběr podle pozic řádků a sloupců

# Pro připomenutí.

mesta

mesta.iloc[2]

mesta.iloc[[2]]

mesta.iloc[2, 1:]

mesta.iloc[[2, 3, 5], [0, 1]]

# ## 3. Ukládání dat

mesta.to_csv("data.csv")

mesta.to_html("data.html")

mesta.to_excel("data.xls")

mesta.to_html("data.html")

mesta.to_json("data.json", indent=4)

# ## A Cvičení



# ## 4. Index

# ![DataFrame](dataframe.svg)

mesta = pandas.read_csv('mesta.csv', encoding='utf-8')
mesta

# Index je teď číselný. Přístup pomocí názvu řádků (`loc`) nebo pomocí jejich čísel (`iloc`) je teď velmi podobný. Jediný rozdíl je v indexování rozsahem.

mesta.loc[:4]

mesta.iloc[:4]

# Index můžeme manuálně nastavit na jeden ze sloupců. Ten potom zmizí z datové části, a přesune se do pozice indexu.

mesta.set_index("mesto")

# ## 5. Dotazy jako v SQL

# Srovnáním DataFrame s tabulkou podobnost s databázemi nekončí. Pandas umožňují dotazovat se nad daty podobným způsobem jako SQL.

mesta = pandas.read_csv("mesta.csv", index_col="mesto", encoding="utf-8")
mesta

# ### Výběr sloupečků

# **SQL:** `SELECT linky, obyvatel FROM mesta;`

mesta[["linky", "obyvatel"]]

# ### Podmínky

# **SQL:** `SELECT * FROM mesta WHERE linky > 10;`

mesta[mesta["linky"] > 10]

# **SQL:** `SELECT kraj, vymera FROM mesta WHERE vymera >= 100 AND vymera <= 200;`

mesta[(mesta["vymera"] >= 100) & (mesta["vymera"] <= 200)][["kraj", "vymera"]]

mesta.loc[(mesta['vymera'] >= 100) & (mesta['vymera'] <= 200), ["kraj", "vymera"]]

# ### Logické operátory v podmínkách

# **SQL:** `SELECT linky FROM mesta WHERE kraj = 'JHM' OR kraj = 'OLK';`

mesta[(mesta['kraj'] == 'JHM') | (mesta['kraj'] == 'OLK')][['linky']]

# **SQL:** `SELECT linky FROM mesta WHERE kraj IN ('JHM', 'ULK', 'OLK');`

mesta[mesta['kraj'].isin(['JHM', 'ULK', 'OLK'])][['linky']]

# **SQL:** `SELECT linky FROM mesta WHERE kraj NOT IN ('JHM', 'ULK', 'OLK');`

mesta[~mesta['kraj'].isin(['JHM', 'ULK', 'OLK'])][['linky']]

# ## 6. Převod mezi DataFrame a seznamy

# ### DataFrame -> seznam

mesta.values.tolist()

# V datech chybí názvy měst. Pandas totiž nebere index jako součást dat, ale jen jako popis tabulky. Je tedy potřeba ho do tabulky nejdřív dostat.

mesta.reset_index()

mesta_seznam = mesta.reset_index().values.tolist()
mesta_seznam

# Pozor, `list(mesta)` nedělá to co bychom čekali.

list(mesta)

# ### Seznam -> DataFrame

pandas.DataFrame(mesta_seznam)

# To funguje, akorát Pandas neví jak pojmenovat sloupce -- v seznamu žádná taková informace není. Pokud se nám nelíbí čísla která automatický dosadí, dodáme názvy sloupců sami.

pandas.DataFrame(mesta_seznam, columns=["mesto", "kraj", "obyvatel", "linky", "vymera"])

# ## B Cvičení


