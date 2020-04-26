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

# ## 01 Základní práce s DataFrame

# ### Načítání dat

# * Pandas umí načítat všechny možné formáty -- CSV, JSON, Excel, HTML, SQL databáze, a spoustu dalších.
# * Rovněž umožňují stáhnout data z internetu -- místo cesty k souboru na disku dáme URL adresu.
# * Podporují kompresi -- ZIP archivy a podobně.

import pandas

# Příklad: tabulka měst provozujících tramvajovou dopravu.

mesta = pandas.read_csv("mesta.csv", index_col="mesto", encoding="utf-8")
mesta

# ### Základní informace o tabulce

# Datové typy, názvy sloupců, počet neprázdných pozorování.

mesta.info()

# Velikost.

mesta.shape

# Názvy sloupců.

mesta.columns

# Základní statistické údaje.

mesta.describe()

# ## 02 Základní selekce

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

# ## 03 Ukládání dat

mesta.to_csv("data.csv")

mesta.to_html("data.html")

mesta.to_excel("data.xls")

mesta.to_html("data.html")

mesta.to_json("data.json", indent=4)

# ## A Cvičení



# ## 04 Index

mesta = pandas.read_csv('mesta.csv', encoding='utf-8')
mesta

mesta.loc[:4]

mesta.iloc[:4]

mesta.set_index("mesto")

# ## 05 Dotazy jako v SQL



# ### Výběr sloupečků



# ### Podmínky



# ### Logické operátory v podmínkách



# ## 06 Převod mezi DataFrame a seznamy



# ## B Cvičení


