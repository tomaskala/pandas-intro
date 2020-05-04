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

# # Agregace

# Pracujeme s datasetem o výsledcích u maturity. Máme k dispozici výsledky ze 3 učeben uložené v souborech `u202.csv`, `u203.csv` a `u302.csv`.

import pandas

# !cat u202.csv

u202 = pandas.read_csv("u202.csv", encoding="utf-8")
u203 = pandas.read_csv("u203.csv", encoding="utf-8")
u302 = pandas.read_csv("u302.csv", encoding="utf-8")

# ## 1. Práce s chybějícími hodnotami

u202

# Na řádcích 0 a 9 je ve sloupci `známka` hodnota `NaN`. Tím se v Pandas značí chybějící hodnota, podobně jako `NULL` v SQL. V samotném CSV souboru údaj chybí úplně, mezi sousedními čárkami nic není.
#
# Všimněte si, že ačkoli je známka celé číslo, sloupec `známka` je uložen jako desetinná čísla. Je to proto, že hodnotu `NaN` není možné reprezentovat v celých číslech. V desetinných (`float`) je pro to naopak vyhrazená hodnota. Podobná situace nastane v případě chybějících pravdivostních hodnot.

# Chybějící hodnoty mohou vzniknout různými způsoby, např.
# * Porucha měřícího přístroje;
# * Chyba při načítání souboru;
# * Hodnota v daném kontextu nedává smysl;
# * Nenastane událost, na kterou čekáme;
# * ...
#
# Často taky nemáme tušení a můžeme jen hádat.
#
# V různých situacích dává smysl vypořádat se s chybějícími hodnotami různými způsoby.

# ### Jak zjistit které hodnoty chybí?

u202["známka"].isnull()

u202.loc[u202["známka"].isnull()]

# ### Počet, procento chybějících hodnot

False + False, False + True, True + True

u202["známka"].isnull().sum()

u202.shape

pocet_radku = u202.shape[0]
relativni_cetnost = u202["známka"].isnull().sum() / pocet_radku
print(f"Chybí {relativni_cetnost * 100} % hodnot.")

relativni_cetnost

u202["známka"].isnull().mean()

# Side note: ten formát co ukazuje 8347359378947389347 desetinných míst není moc čitelný.

print(f"Chybí {relativni_cetnost * 100:.02f} % hodnot.")

# Mnohem lepší.

# ### Jak zahodit řádky s chybějícími hodnotami?

u202

u202.dropna()

# Lze přizpůsobit dalšími argumenty - minimální počet chybějících hodnot, uvažovat jen vybrané sloupce, ...

# ### Jak zahodit sloupce s chybějícícmi hodnotami?

u202

u202.dropna(axis="columns")

# ### Jak nahradit chybějící hodnoty něčím jiným?

u202

doplneno = u202.fillna(5)
doplneno

doplneno["známka"] = doplneno["známka"].astype(int)
doplneno

# ### Někdy to ani není třeba

# * Může se stát, že se sloupci, ve kterých chybí hodnoty, ani nepotřebujeme pracovat. Bylo by pak zbytečné zahazovat nějaké řádky, protože bychom tím přišli o data.
# * Pandas funkce umí s chybějícími hodnotami pracovat.

u202["známka"]

u202["známka"].mean()

# ## 2. Spojení dat

# Máme k dispozici údaje o maturitách ve všech 3 místnostech, chtěli bychom je spojit dohromady do jednoho dataframe.
#
# Nejprve zahodíme studenty, kteří nedorazili ke zkoušce.

u202.dropna(inplace=True)
u203.dropna(inplace=True)
u302.dropna(inplace=True)

maturita = pandas.concat([u202, u203, u302])
maturita.head(16)

# Pandas napojilo indexy jednotlivých dataframes dohromady, takže jsou tam duplicity.

maturita = pandas.concat([u202, u203, u302], ignore_index=True)
maturita.head(16)

# Ještě budeme chtít uchovat informaci o místnostech, ve kterých zkoušky probíhaly.

u202["místnost"] = "u202"
u203["místnost"] = "u203"
u302["místnost"] = "u302"

maturita = pandas.concat([u202, u203, u302], ignore_index=True)
maturita.head(16)

# Výsledný dataframe uložíme do CSV souboru.

maturita.to_csv("maturita.csv", index=False)

# !cat maturita.csv

# ## 3. Joinování dat

# Obdobou SQL příkazu `JOIN` je v Pandas funkce `merge`. K datasetu výsledků u maturitních zkoušek budeme joinovat data o předsedajících maturitních komisí v jednotlivých dnech.

# !cat predsedajici.csv

preds = pandas.read_csv("predsedajici.csv", encoding="utf-8")
preds

# Vyzkoušíme merge, zatím jen na místnosti u202.

u202

test = pandas.merge(u202, preds)
test

# Dostali jsme prázdný dataframe. To je proto, že defaultně `merge` dělá `INNER JOIN` přes všechny sloupce se stejnými jmény, zde `jméno` a `den`. Protože jedno `jméno` odpovídá studentovi a druhé předsedovi, nemáme žádný průnik.
#
# Nabízel by se `OUTER JOIN`, ale ten nepomůže.

test = pandas.merge(u202, preds, how="outer")
test

# Tím se nám akorát promíchala jména studentů a předsedajících, navíc vznikla spousta nedefinovaných hodnot.

# Ve skutečnosti potřebujeme provést `JOIN` jen podle sloupce `den` -- ke každému dni známe předsedu komise a všechny studenty, kteří měli ten den zkoušku.

test = pandas.merge(u202, preds, on="den")
test

# Skoro dobré, jen potřebujeme rozumně přejmenovat sloupce se jmény na jméno studenta a jméno předsedy.

test = test.rename(columns={"jméno_x": "jméno_student", "jméno_y": "jméno_předseda"})
test

# To už vypadá dobře, provedeme tedy `JOIN` pro celý dataset a výsledek opět uložíme do CSV.

maturita2 = pandas.merge(maturita, preds, on="den")
maturita2 = maturita2.rename(columns={"jméno_x": "jméno_student", "jméno_y": "jméno_předseda"})
maturita2.head()

maturita2.to_csv("maturita2.csv", index=False)

# ## 4. Grupování

# Pandí obdoba databázové operace `GROUP BY` se nazývá... `groupby`.

maturita2.head()

groups = maturita2.groupby("místnost")

# Jak to vypadá?

groups

# Wtf

for key, item in groups:
    print(key)
    display(item)

# Aha!

groups.count()

# Můžeme si spočítat průměrnou známku přes předměty.

# Jako series.

maturita2.groupby('předmět')['známka'].mean()

# Jako dataframe.

maturita2.groupby('předmět')[['známka']].mean()

# Pandy nejsou blbé a průměry počítají jen z numerických sloupců, což je v našem případě jen `známka`.

maturita2.groupby('předmět').mean()

# Další agregační funkce jsou např.
# * `sum` - součet hodnot
# * `max` - maximální hodnota
# * `min` - minimální hodnota
# * `first` - první hodnota
# * `last` - poslední hodnota
# * `mean` - průměr z hodnot
# * `median` - medián z hodnot
# * `var` - rozptyl hodnot
# * `std` - standardní odchylka hodnot
# * `all` - True, pokud jsou všechny hodnoty True
# * `any` - True, pokud je alespoň jedna z hodnot True

# Můžeme se podívat, jak vypadaly známky mezi jednotlivými předsedy komise.

groups_preds = maturita2.groupby("jméno_předseda")

groups_preds.mean()

groups_preds.median()

groups_preds.std()

# Když chceme víc agregací najednou, můžeme použít funkci `agg` a dát jí seznam názvů funkcí, které chceme aplikovat.

groups_preds.agg(["mean", "median", "std"])


