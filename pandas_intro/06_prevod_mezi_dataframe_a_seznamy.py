import pandas

mesta = pandas.read_csv("mesta.csv", index_col="mesto", encoding="utf-8")

# ## 6. Převod mezi DataFrame a seznamy

# ### DataFrame -> seznam

print(mesta.values.tolist())

# V datech chybí názvy měst. Pandas totiž nebere index jako součást dat, ale jen jako popis tabulky. Je tedy potřeba ho do tabulky nejdřív dostat.

print(mesta.reset_index())

mesta_seznam = mesta.reset_index().values.tolist()
print(mesta_seznam)

# Pozor, `list(mesta)` nedělá to co bychom čekali.

print(list(mesta))

# ### Seznam -> DataFrame

print(pandas.DataFrame(mesta_seznam))

# To funguje, akorát Pandas neví jak pojmenovat sloupce -- v seznamu žádná taková informace není. Pokud se nám nelíbí čísla která automatický dosadí, dodáme názvy sloupců sami.

print(pandas.DataFrame(mesta_seznam, columns=["mesto", "kraj", "obyvatel", "linky", "vymera"]))
