import pandas

# ## 5. Dotazy jako v SQL

# Srovnáním DataFrame s tabulkou podobnost s databázemi nekončí. Pandas umožňují dotazovat se nad daty podobným způsobem jako SQL.
#
# Vrátíme názvy měst jako index pro lepší srozumitelnost.

mesta = pandas.read_csv("mesta.csv", index_col="mesto", encoding="utf-8")
print(mesta)

# ### Výběr sloupečků

# **SQL:** `SELECT linky, obyvatel FROM mesta;`

print(mesta[["linky", "obyvatel"]])

# ### Podmínky

# **SQL:** `SELECT * FROM mesta WHERE linky > 10;`

print(mesta[mesta["linky"] > 10])

# **SQL:** `SELECT kraj, vymera FROM mesta WHERE vymera >= 100 AND vymera <= 200;`

print(mesta[(mesta["vymera"] >= 100) & (mesta["vymera"] <= 200)][["kraj", "vymera"]])

print(mesta.loc[(mesta['vymera'] >= 100) & (mesta['vymera'] <= 200), ["kraj", "vymera"]])

# ### Logické operátory v podmínkách

# **SQL:** `SELECT linky FROM mesta WHERE kraj = 'JHM' OR kraj = 'OLK';`

print(mesta[(mesta['kraj'] == 'JHM') | (mesta['kraj'] == 'OLK')][['linky']])

# **SQL:** `SELECT linky FROM mesta WHERE kraj IN ('JHM', 'ULK', 'OLK');`

print(mesta[mesta['kraj'].isin(['JHM', 'ULK', 'OLK'])][['linky']])

# **SQL:** `SELECT linky FROM mesta WHERE kraj NOT IN ('JHM', 'ULK', 'OLK');`

print(mesta[~mesta['kraj'].isin(['JHM', 'ULK', 'OLK'])][['linky']])
