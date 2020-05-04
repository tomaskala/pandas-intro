import pandas

# a.
studenti1 = pandas.read_csv("studenti1.csv", encoding="utf-8")
studenti2 = pandas.read_csv("studenti2.csv", encoding="utf-8")
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
print(studenti)
print()

# b.
pocet_nestudujicich = studenti["ročník"].isnull().sum()
pocet_dalkovych = studenti["kruh"].isnull().sum()
print(f"Nestuduje {pocet_nestudujicich} studentů.")
print(f"Dálkově studuje {pocet_dalkovych} studentů.")

# c.
# Celkove bylo 33 nestudujicich a 27 dalkovych studentu, celkove tedy 60
# chybejicich hodnot.
# Tato funkce zahodi pouze 58 hodnot. Nejde o chybu, 2 studenti byli dalkovi
# a uz nestuduji, tedy jim chybel jak rocnik, tak kruh.
prezencni = studenti.dropna()
print(prezencni)
print()

# d.
print(prezencni.groupby("obor")["jméno"].count())
print()

# e.
print(prezencni.groupby("obor")["prospěch"].mean())
print()

# f.
jmena = pandas.read_csv("jmena100.csv")
joined = pandas.merge(prezencni, jmena, on="jméno")
print(joined)
print()

# g.
print(joined.groupby("pohlaví")["jméno"].count())
