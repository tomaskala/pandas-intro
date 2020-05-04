import pandas

u202 = pandas.read_csv("u202.csv", encoding="utf-8")
u203 = pandas.read_csv("u203.csv", encoding="utf-8")
u302 = pandas.read_csv("u302.csv", encoding="utf-8")

# ## 2. Spojení dat

# Máme k dispozici údaje o maturitách ve všech 3 místnostech, chtěli bychom je spojit dohromady do jednoho dataframe.
#
# Nejprve zahodíme studenty, kteří nedorazili ke zkoušce.

u202.dropna(inplace=True)
u203.dropna(inplace=True)
u302.dropna(inplace=True)

maturita = pandas.concat([u202, u203, u302])
print(maturita.head(16))

# Pandas napojilo indexy jednotlivých dataframes dohromady, takže jsou tam duplicity.

maturita = pandas.concat([u202, u203, u302], ignore_index=True)
print(maturita.head(16))

# Ještě budeme chtít uchovat informaci o místnostech, ve kterých zkoušky probíhaly.

u202["místnost"] = "u202"
u203["místnost"] = "u203"
u302["místnost"] = "u302"

maturita = pandas.concat([u202, u203, u302], ignore_index=True)
print(maturita.head(16))

# Výsledný dataframe uložíme do CSV souboru.

maturita.to_csv("maturita.csv", index=False)
