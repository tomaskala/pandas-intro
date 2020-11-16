import pandas

vaha = pandas.read_csv("vaha.txt", encoding="utf-8", sep="\t")
dny = vaha["den"]
cislo_dne = dny.str[3:]
cislo_dne = cislo_dne.str.replace(".", "")
cislo_dne = pandas.to_numeric(cislo_dne)
nazev_dne = dny.str[:2]
vaha.drop("den", axis="columns", inplace=True)
vaha["číslo_dne"] = cislo_dne
vaha["název_dne"] = nazev_dne

# ## 3. Chroustání Series

# Zde budeme transformovat sloupec `váha`.

print(vaha)


# Jak se píše na kodim.cz: *Pokud se nám podaří rozdělit hodnotu podle mezery, můžeme první část převést na číslo. Pokud se to nepovede, můžeme dělit podle písmenka 'k'*
#
# Tento postup si definujeme jako funkci, kterou aplikujeme na sloupec `váha` prvek po prvku.

def prevod_vahy(vaha):
    casti = vaha.split(" ")
    
    if len(casti) < 2:
        casti = vaha.split("k")
        
    desetinna_tecka = casti[0].replace(",", ".")
    return float(desetinna_tecka)


# Takto definovanou funkci nyní použijeme jako parametr funkce `apply` volané na sloupci `váha`. Funkce `apply` vezme námi definovanou funkci, a aplikuje ji na každý prvek daného sloupce. Výsledkem je sloupec výsledků naší funkce.

vaha["váha"] = vaha["váha"].apply(prevod_vahy)
print(vaha)

print(vaha.dtypes)


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
print(vaha)

print(vaha.dtypes)
