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

# # Transformace

# ![transformace](transformace.png)

# ## 1. Vlastní funkce

# Příklad: funkce `round`, `len`, `random`, `open`.
#
# * Funkce je poměrně základním konceptem v Pythonu a programování vůbec.
# * Dosud jsme jich potkali spoustu, jak přímo z Pythonu nebo z nějaké knihovny (`requests`, `pandas`, ...).
# * Je možné definovat si vlastní funkce.
#
#
# * Umožňuje definovat blok kódu provádějící určitou specializovanou činnost, která se opakuje.
# * Přesné chování funkce je závislé na vstupních parametrech.
# * Vrací hodnotu jako výsledek.

# ![triangle](triangle-area.png)

# Z kodim.cz ukradneme nápad na funkci pro výpočet obsahu trojúhelníku.

# +
height1 = 3
width1 = 6
area1 = (height1 * width1) / 2
print(area1)

height2 = 4
width2 = 3
area2 = (height2 * width2) / 2
print(area2)


# -

# Pokud potřebujeme spočítat obsah mnoha trojúhelníků, začne být otravné vypisovat pořád ten samý kód dokola. Navíc při častém opisování toho samého snadno uděláme chybu.
#
# Definujeme si funkci, která v parametrech dostane rozměry trojúhelníku a jako výsledek vrátí jeho obsah.

def triangle_area(height, width):
    return (height * width) / 2


# +
area1 = triangle_area(3, 6)
print(area1)

area2 = triangle_area(4, 3)
print(area2)


# -

# Formát definice funkce je následující.
# ```
# def <nazev_funkce>(<parametry>):
#     <libovolny kod>
# ```
#
# * Názvy funkcí se řídí stejnými pravidly, jako názvy proměnných.
# * Funkce může mít libovolný počet parametrů. Pokud nemá žádné, kulaté závorky necháme prázdné (být tam ale musejí).
# * Uvnitř těla funkce (odsazené pod jejím názvem a parametry) může být libovolný kód.
# * Proměnné definované uvnitř funkce existují pouze tam, zvenčí nejsou viditelné.
# * Pokud funkce vrací nějaký výsledek, uvedeme na konci `return <vysledek>`.

# ### Součet kladných hodnot

def sum_positive(values):
    result = 0
    
    for value in values:
        if value > 0:
            result += value
            
    return result


test1 = [1, 2, 3, 4, 5]
python_sum1 = sum(test1)
my_sum1 = sum_positive(test1)
print(f"Python sum: {python_sum1}")
print(f"My sum: {my_sum1}")

test2 = [-1, 2, 3, -4, 5]
python_sum2 = sum(test2)
my_sum2 = sum_positive(test2)
print(f"Python sum: {python_sum2}")
print(f"My sum: {my_sum2}")


# ### Zápis do CSV
# Funkce bez návratové hodnoty. Pozor, je velmi zjednodušená, v praxi by se měly použít pandas nebo pythonovský modul pro práci s CSV soubory.

def write_to_csv(path, values):
    f = open(path, mode="w", encoding="utf-8")
    
    for value in values:
        f.write(",".join(value))
        f.write("\n")
    
    f.close()


data = [["hello", "python"], ["goodbye", "python"]]
write_to_csv("test.csv", data)

# !cat test.csv

# ### Převod školních známek
# Funkce mohou také zpřehlednit kód. Použijeme příklad z dřívejška s převodem známek z písmen na čísla.

grades = ["A", "A", "B", "A", "C", "D", "E", "C", "B", "A", "C"]

converted1 = [grade.replace("A", "1").replace("B", "2").replace("C", "3").replace("D", "4").replace("E", "5")
              for grade in grades]
print(converted1)


def convert_grade(grade):
    return grade.replace("A", "1").replace("B", "2").replace("C", "3").replace("D", "4").replace("E", "5")


converted2 = [convert_grade(grade) for grade in grades]
print(converted2)


def convert_grade_better(grade):
    if grade == "A":
        return "1"
    elif grade == "B":
        return "2"
    elif grade == "C":
        return "3"
    elif grade == "D":
        return "4"
    else:
        return "5"


converted3 = [convert_grade_better(grade) for grade in grades]
print(converted3)

# ## Cvičení



# ## 2. Transformace dat v Pandas

# Pracujeme s daty o hmotnosti Kristiána během 14 dnů, kdy se snažil zhubnout.

# !cat vaha.txt

import pandas

vaha = pandas.read_csv("vaha.txt", encoding="utf-8", sep="\t")
vaha

vaha.dtypes

# Conclusion: Kristián je trochu prase, aneb data v praxi.

# Nejprve transformujeme sloupec `den` na číslo dne. Sloupec `den` je uložen vždy jako `2pismenny_nazev_dne cislo_dne`, některá čísla navíc končí tečkou.

# ### Zahodíme názvy dnů

dny = vaha["den"]
dny

cislo_dne = dny.str[3:]
cislo_dne

# Alternativy: `split`, `replace`.

# ### Zahodíme tečky

cislo_dne = cislo_dne.str.replace(".", "")
cislo_dne

# ### Převedeme na čísla

cislo_dne = pandas.to_numeric(cislo_dne)
cislo_dne

# ### Uložíme ještě název dne

dny

nazev_dne = dny.str[:2]
nazev_dne

# ### Obojí uložíme do dataframe

vaha.drop("den", axis="columns", inplace=True)
vaha

vaha["číslo_dne"] = cislo_dne
vaha["název_dne"] = nazev_dne
vaha

vaha.dtypes

# Tím máme slušně uložené údaje o dnech.

# ## 3. Chroustání Series

# Zde budeme transformovat sloupec `váha`.

vaha


# Jak se píše na kodim.cz: *Pokud se nám podaří rozdělit hodnotu podle mezery, můžeme první část převést na číslo. Pokud se to nepovede, můžeme dělit podle písmenka 'k'*
#
# Tento postup si definujeme jako funkci, kterou aplikujeme na sloupec `váha` prvek po prvku.

def prevod_vahy(vaha):
    casti = vaha.split(" ")
    
    if len(casti) < 2:
        casti = vaha.split("k")
        
    desetinna_tecka = casti[0].replace(",", ".")
    return float(desetinna_tecka)


# Takto definovanou funkci nyní použijeme jako parametr funkce `apply` volané na sloupci `váha`.

vaha["váha"] = vaha["váha"].apply(prevod_vahy)
vaha

vaha.dtypes


# Ještě by bylo fajn upravit sloupec `běh`.

def prevod_behu(beh):
    if beh == "pauza" or beh == "paza":
        return 0
    elif pandas.isnull(beh):
        return beh
    else:
        casti = beh.split(" ")
        
        if len(casti) < 2:
            casti = beh.split("k")
            
        return float(casti[0])


vaha["běh"] = vaha["běh"].apply(prevod_behu)
vaha

vaha.dtypes

# ## 4. Vlastní agregační funkce

# Definujeme si vlastní agregační funkci, podobně jako jsme posledně viděli funkce `mean`, `std` a podobné, volané na výsledku operace `groupby`.

# Data seskupíme podle týdne a v každém týdnu napočítáme nějakou funkci váhy. Zde např. průměrnou váhu v každém týdnu.

vaha.groupby("týden")["váha"].mean()


# Budeme počítat tzv. rozpětí (spread) -- rozdíl mezi maximální a minimální hodnotou. Takovou funkci pandas nenabízí, musíme si ji tedy napsat sami.
#
# Funkce jako argument dostane pandas series (sloupec) a jako výsledek vrátí jeho rozpětí.

def spread(series):
    return series.max() - series.min()


# Nejprve funkci aplikujeme na jediný sloupec. Tím dostaneme rozpětí vah za celé sledované období.

vaha["váha"].agg(spread)

# A teď na groupby objekt -- za každý týden dostaneme rozpětí vah.

vaha.groupby("týden")["váha"].agg(spread)


