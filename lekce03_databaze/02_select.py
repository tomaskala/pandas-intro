# ## 2. SELECT

# ### Připojení a základní SELECTy

# Zatím jsme si vyráběli SQL dotazy ve stringu, ale neposílali jsme je do databáze. To přijde teď.


import pandas as pd
import snowflake.connector


# Nejprve potřebujeme zadat jméno a heslo pro přístup do databáze. Formálně je potřeba i role, ale zde víme jak vypadá, tak ji dostaneme automaticky.


name = ...  # Dopln svuj login jako string.
password = ...  # Dopln svoje heslo jako string.
role = "ROLE_" + name.upper()


# Doplníme údaje o databázovém serveru a pomocí Snowflake connectoru navážeme spojení.


DATABASE = "COURSES"
HOST = "https://ip68917.eu-west-1.snowflakecomputing.com/"
SCHEMA = "SCH_CZECHITA"
WAREHOUSE = "COMPUTE_WH"
ACCOUNT = "ip68917.eu-west-1"

conn = snowflake.connector.connect(
    user=name,
    password=password,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA,
    role=role,
)


# Vyzkoušíme jednoduchý SQL dotaz -- vybereme všechny státy z tabulky `country` ve schématu `SCH_CZECHITA`. Výsledkem je obyčejný Pandas dataframe.


sql = """
SELECT *
FROM SCH_CZECHITA.country
"""

print(pd.read_sql_query(sql, conn))


# Protože jsme schéma uvedli už při připojení, nemusíme ho opakovat u každé tabulky.


sql = """
SELECT *
FROM country
"""

print(pd.read_sql_query(sql, conn))


# Podobně jako při načítání souboru můžeme nějaký sloupec použít jako index. Typicky se k tomu hodí primární klíč.


sql = """
SELECT *
FROM country
"""

print(pd.read_sql_query(sql, conn, index_col="ID"))


# ### Porovnání SQL a Pandas

# Teď si ukážeme jak by vypadal stejný dotaz v SQL a v Pandas. Vybereme počet mrtvých (`nkill`) a zemi (`country_txt`) z tabulky `teror` ze všech útoků, kde někdo zemřel a staly se v Iráku nebo v Sýrii. Protože je jich hodně, omezíme se jen na prvních 100 nejsmrtelnějších.


sql = """
SELECT nkill,
       country_txt
FROM teror
WHERE nkill > 0
  AND country_txt IN ('Iraq', 'Syria')
ORDER BY nkill DESC
LIMIT 100
"""

print(pd.read_sql_query(sql, conn))



sql = """
SELECT *
FROM teror
"""

df = pd.read_sql_query(sql, conn)

nekdo_zemrel = df["NKILL"] > 0
zadana_zeme = df["COUNTRY_TXT"].isin(["Syria", "Iraq"])
zadane_sloupce = ["NKILL", "COUNTRY_TXT"]

print(df.loc[nekdo_zemrel & zadana_zeme, zadane_sloupce].sort_values(by="NKILL", ascending=False).head(100))


# Vidíme, že výsledek je téměř stejný. Jediný rozdíl je v datových typech - počet mrtvých z SQL je v celých číslech, pandy nám to daly jako floaty. Z minulé lekce můžeme tušit, že by tam mohly být nějaké chybějící hodnoty.


print(df["NKILL"].isna().sum())


# Je to tak. Chybějící hodnoty byly v tabulce ještě před protříděním, proto se nám datový typ float propagoval až na konec. Když jsme výsledek získali jako SQL dotaz, do Pandas dorazila jen výsledná tabulka 100 nejsmrtelnějších útoků, ve které nic nechybí.

# O něco fundamentálnější rozdíl je v přístupu k datům. Pokud zadáme celý dotaz v SQL, celý výpočet běží na databázovém serveru. Pokud použijeme Pandas, běží výpočet na našem počítači. Navíc je s tím spojená práce navíc -- abychom dostali data pro Pandas, museli jsme selectnout úplně celou tabulku.
# 
# Tohle byl demonstrační příklad. V praxi bychom preferovali nechat maximum práce na databázi, aby k nám do počítače šlo co nejmenší množství dat. Pandas (případně jiné Pythonovské knihovny) pak použijeme na tento pročitěný dataset. To nám umožňí provést operace, které SQL buď přímo nepodporuje, nebo jsou v něm zbytečně těžkopádné.

# ### UNION

# Na závěr si ukážeme `UNION` a už zmínené formátování stringů.

# Budeme chtít vybrat všechny názvy zbraní (`weaptype.name`) ať už byly při útoku použity jako primární nebo sekundární. K tabulce `teror2` je joinneme pomocí sloupců `teror2.weaptype1`, respektive `teror2.weaptype2` a sloupce `weaptype.id`.


sql = """
SELECT w.name 
FROM teror2 t
JOIN weaptype w
ON t.weaptype1 = w.id
UNION
SELECT w.name 
FROM teror2 t
JOIN weaptype w
ON t.weaptype2 = w.id
"""

print(pd.read_sql(sql, conn))


# Vidíme, že oba dotazy jsou skoro stejné, liší se jen sloupcem `t.weaptype1` nebo `t.weaptype2`. Nabízí se tedy poskládat dotaz z více částí.


select_sql = """
SELECT w.name
FROM teror2 t
JOIN weaptype w
ON t.{column} = w.id
"""

union_sql = f"""
{select_sql.format(column='weaptype1')}
UNION
{select_sql.format(column='weaptype2')}
"""

print(union_sql)



print(pd.read_sql_query(union_sql, conn))

conn.close()
