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

def prevod_vahy(vaha):
    casti = vaha.split(" ")
    
    if len(casti) < 2:
        casti = vaha.split("k")
        
    desetinna_tecka = casti[0].replace(",", ".")
    return float(desetinna_tecka)

vaha["váha"] = vaha["váha"].apply(prevod_vahy)

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

# ## 4. Vlastní agregační funkce

# Definujeme si vlastní agregační funkci, podobně jako jsme posledně viděli funkce `mean`, `std` a podobné, volané na výsledku operace `groupby`.

# Data seskupíme podle týdne a v každém týdnu napočítáme nějakou funkci váhy. Zde např. průměrnou váhu v každém týdnu.

print(vaha.groupby("týden")["váha"].mean())


# Budeme počítat tzv. rozpětí (spread) -- rozdíl mezi maximální a minimální hodnotou. Takovou funkci pandas nenabízí, musíme si ji tedy napsat sami.
#
# Funkce jako argument dostane pandas series (sloupec) a jako výsledek vrátí jeho rozpětí.

def spread(series):
    return series.max() - series.min()


# Nejprve funkci aplikujeme na jediný sloupec. Tím dostaneme rozpětí vah za celé sledované období.

print(vaha["váha"].agg(spread))

# A teď na groupby objekt -- za každý týden dostaneme rozpětí vah.

print(vaha.groupby("týden")["váha"].agg(spread))
