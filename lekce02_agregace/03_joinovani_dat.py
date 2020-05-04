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

# ## 3. Joinování dat

# Obdobou SQL příkazu `JOIN` je v Pandas funkce `merge`. K datasetu výsledků u maturitních zkoušek budeme joinovat data o předsedajících maturitních komisí v jednotlivých dnech.

preds = pandas.read_csv("predsedajici.csv", encoding="utf-8")
print(preds)

# Vyzkoušíme merge, zatím jen na místnosti u202.

print(u202)

test = pandas.merge(u202, preds)
print(test)

# Dostali jsme prázdný dataframe. To je proto, že defaultně `merge` dělá `INNER JOIN` přes všechny sloupce se stejnými jmény, zde `jméno` a `den`. Protože jedno `jméno` odpovídá studentovi a druhé předsedovi, nemáme žádný průnik.
#
# Nabízel by se `OUTER JOIN`, ale ten nepomůže.

test = pandas.merge(u202, preds, how="outer")
print(test)

# Tím se nám akorát promíchala jména studentů a předsedajících, navíc vznikla spousta nedefinovaných hodnot.

# Ve skutečnosti potřebujeme provést `JOIN` jen podle sloupce `den` -- ke každému dni známe předsedu komise a všechny studenty, kteří měli ten den zkoušku.

test = pandas.merge(u202, preds, on="den")
print(test)

# Skoro dobré, jen potřebujeme rozumně přejmenovat sloupce se jmény na jméno studenta a jméno předsedy.

test = test.rename(columns={"jméno_x": "jméno_student", "jméno_y": "jméno_předseda"})
print(test)

# To už vypadá dobře, provedeme tedy `JOIN` pro celý dataset a výsledek opět uložíme do CSV.

maturita2 = pandas.merge(maturita, preds, on="den")
maturita2 = maturita2.rename(columns={"jméno_x": "jméno_student", "jméno_y": "jméno_předseda"})
print(maturita2.head())

maturita2.to_csv("maturita2.csv", index=False)
