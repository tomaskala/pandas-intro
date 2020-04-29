import pandas

df = pandas.read_csv("jmena100.csv", encoding="utf-8")

# a.
print(df[df["věk"] > 60])
print()

# b.
print(df[(80000 < df["četnost"]) & (df["četnost"] < 100000)])
print()

# c.
# pomoci isin
slovansky_hebrejsky1 = df[df["původ"].isin(["slovanský", "hebrejský"])]
pocet_jmen1 = slovansky_hebrejsky1.shape[0]
print(slovansky_hebrejsky1)
print()
print(pocet_jmen1)
print()

# pomoci jedno | (OR) druhe
slovansky_hebrejsky2 = df[(df["původ"] == "slovanský") | (df["původ"] == "hebrejský")]
pocet_jmen2 = slovansky_hebrejsky2.shape[0]
print(slovansky_hebrejsky2)
print()
print(pocet_jmen2)
print()

# d.
unor = df[df["svátek"].isin(["1.2", "2.2", "3.2", "4.2", "5.2", "6.2", "7.2"])]
print(unor["jméno"])
