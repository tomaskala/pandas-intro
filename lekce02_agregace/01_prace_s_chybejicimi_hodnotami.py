# # Agregace

# Pracujeme s datasetem o výsledcích u maturity. Máme k dispozici výsledky ze 3 učeben uložené v souborech `u202.csv`, `u203.csv` a `u302.csv`.

import pandas

u202 = pandas.read_csv("u202.csv", encoding="utf-8")
u203 = pandas.read_csv("u203.csv", encoding="utf-8")
u302 = pandas.read_csv("u302.csv", encoding="utf-8")

# ## 1. Práce s chybějícími hodnotami

print(u202)

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

print(u202["známka"].isnull())

print(u202.loc[u202["známka"].isnull()])

# ### Počet, procento chybějících hodnot

print(False + False, False + True, True + True)

print(u202["známka"].isnull().sum())

print(u202.shape)

pocet_radku = u202.shape[0]
relativni_cetnost = u202["známka"].isnull().sum() / pocet_radku
print(f"Chybí {relativni_cetnost * 100} % hodnot.")

print(relativni_cetnost)

print(u202["známka"].isnull().mean())

# Side note: ten formát co ukazuje 8347359378947389347 desetinných míst není moc čitelný.

print(f"Chybí {relativni_cetnost * 100:.02f} % hodnot.")

# Mnohem lepší.

# ### Jak zahodit řádky s chybějícími hodnotami?

print(u202)

print(u202.dropna())

# Lze přizpůsobit dalšími argumenty - minimální počet chybějících hodnot, uvažovat jen vybrané sloupce, ...

# ### Jak zahodit sloupce s chybějícícmi hodnotami?

print(u202)

print(u202.dropna(axis="columns"))

# ### Jak nahradit chybějící hodnoty něčím jiným?

print(u202)

doplneno = u202.fillna(5)
print(doplneno)

doplneno["známka"] = doplneno["známka"].astype(int)
print(doplneno)

# ### Někdy to ani není třeba

# * Může se stát, že se sloupci, ve kterých chybí hodnoty, ani nepotřebujeme pracovat. Bylo by pak zbytečné zahazovat nějaké řádky, protože bychom tím přišli o data.
# * Pandas funkce umí s chybějícími hodnotami pracovat.

print(u202["známka"])

print(u202["známka"].mean())

