# ## 2. Transformace dat v Pandas

# Budeme se snažit převést špatně formátovaná data do tvaru, se kterým se lépe pracuje. Něco takového řešíme v praxi v jednom kuse -- dostaneme horu dat, nic o nich nevíme a potřebujeme v nich udělat pořádek.
#
# Pracujeme s daty o hmotnosti Kristiána během 14 dnů, kdy se snažil zhubnout.

# !cat vaha.txt

import pandas

vaha = pandas.read_csv("vaha.txt", encoding="utf-8", sep="\t")
print(vaha)

print(vaha.dtypes)

# Conclusion: Kristián je trochu prase, aneb data v praxi.

# Nejprve transformujeme sloupec `den` na číslo dne. Sloupec `den` je uložen vždy jako `2pismenny_nazev_dne cislo_dne`, některá čísla navíc končí tečkou.

# ### Zahodíme názvy dnů

dny = vaha["den"]
print(dny)

cislo_dne = dny.str[3:]
print(cislo_dne)

# ### Zahodíme tečky

cislo_dne = cislo_dne.str.replace(".", "")
print(cislo_dne)

# ### Převedeme na čísla

cislo_dne = pandas.to_numeric(cislo_dne)
print(cislo_dne)

# ### Uložíme ještě název dne

print(dny)

nazev_dne = dny.str[:2]
print(nazev_dne)

# ### Obojí uložíme do dataframe

vaha.drop("den", axis="columns", inplace=True)
print(vaha)

vaha["číslo_dne"] = cislo_dne
vaha["název_dne"] = nazev_dne
print(vaha)

print(vaha.dtypes)

# Tím máme slušně uložené údaje o dnech.
