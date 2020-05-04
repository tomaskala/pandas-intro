import pandas

u202 = pandas.read_csv("u202.csv", encoding="utf-8")
u203 = pandas.read_csv("u203.csv", encoding="utf-8")
u302 = pandas.read_csv("u302.csv", encoding="utf-8")

u202.dropna(inplace=True)
u203.dropna(inplace=True)
u302.dropna(inplace=True)

u202["místnost"] = "u202"
u203["místnost"] = "u203"
u302["místnost"] = "u302"

maturita = pandas.concat([u202, u203, u302], ignore_index=True)

preds = pandas.read_csv("predsedajici.csv", encoding="utf-8")

maturita2 = pandas.merge(maturita, preds, on="den")
maturita2 = maturita2.rename(columns={"jméno_x": "jméno_student", "jméno_y": "jméno_předseda"})

# ## 4. Grupování

# Pandí obdoba databázové operace `GROUP BY` se nazývá... `groupby`.

print(maturita2.head())

groups = maturita2.groupby("místnost")

# Jak to vypadá?

print(groups)

# Wtf

for key, item in groups:
    print(key)
    print(item)

# Aha!

print(groups.count())

# Můžeme si spočítat průměrnou známku přes předměty.

# Jako series.

print(maturita2.groupby('předmět')['známka'].mean())

# Jako dataframe.

print(maturita2.groupby('předmět')[['známka']].mean())

# Pandy nejsou blbé a průměry počítají jen z numerických sloupců, což je v našem případě jen `známka`.

print(maturita2.groupby('předmět').mean())

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

print(groups_preds.mean())

print(groups_preds.median())

print(groups_preds.std())

# Když chceme víc agregací najednou, můžeme použít funkci `agg` a dát jí seznam názvů funkcí, které chceme aplikovat.

print(groups_preds.agg(["mean", "median", "std"]))
