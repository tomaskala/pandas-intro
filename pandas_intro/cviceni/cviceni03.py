import pandas

# a.
df = pandas.read_csv("jmena100.csv", encoding="utf-8")

# b.
df_vybrane_puvody = df[~df["původ"].isin(["hebrejský", "aramejský", "slovanský"])]
df_jmena_cetnosti = df_vybrane_puvody[["jméno", "četnost"]]
print(df_jmena_cetnosti)
print()

# c.
seznam = df_jmena_cetnosti.values.tolist()
celkova_cetnost = sum(jmeno_cetnost[1] for jmeno_cetnost in seznam)
print(celkova_cetnost)
print()

# d.
# Nevim jestli se po nas chce procentualni zastoupeni vsech jmen dohromady
# nebo zvlast. Tady je pro jistotu oboji.
pocet_obyvatel = 10629798
dohromady = celkova_cetnost / pocet_obyvatel * 100.0
print(f"Relativni cetnost dohromady: {dohromady} %.")
print()

print("Relativni cetnost zvlast:")

for jmeno_cetnost in seznam:
    jmeno = jmeno_cetnost[0]
    cetnost = jmeno_cetnost[1]
    relativni_cetnost = cetnost / pocet_obyvatel * 100.0
    print(f"Relativni cetnost jmena {jmeno} je {relativni_cetnost} %.")

# Poznamka pro ty, komu prijde odporne videt ta procenta na milion
# desetinnych mist.
# Lze psat `print(f"Relativni cetnost je {dohromady:.02f} %.")`. Tim dostaneme
# napr. 2 desetinna mista. Pomoci {dohromady:.03f} bychom dostali 3, atd.
