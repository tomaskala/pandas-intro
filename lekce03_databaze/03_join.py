import pandas as pd
import snowflake.connector


name = ...  # Dopln svuj login jako string.
password = ...  # Dopln svoje heslo jako string.
role = "ROLE_" + name.upper()


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


# ## 3. JOIN

# Opět si porovnáme JOIN mezi SQL a Pandas.

# Vybereme název státu (`country.name`) a typ útoku (`attacktype.name`) tak, že k tabulce `teror2` najoinujeme tabulku `country` přes `teror2.country` <-> `country.id` a tabulku `attacktype` přes `teror2.attacktype1` <-> `attacktype.id`. Pro urychlení opět jen prvních 100 záznamů.


sql = """
SELECT c.name AS country_name,
       atyp.name AS attack_name
FROM teror2 AS t
LEFT JOIN country AS c
ON t.country = c.id
LEFT JOIN attacktype AS atyp
ON t.attacktype1 = atyp.id
LIMIT 100;
"""

print(pd.read_sql_query(sql, conn))



sql_teror2 = """
SELECT *
FROM teror2
"""

sql_country = """
SELECT *
FROM country
"""

sql_attacktype = """
SELECT *
FROM attacktype
"""

df_teror2 = pd.read_sql_query(sql_teror2, conn)
df_country = pd.read_sql_query(sql_country, conn)
df_attacktype = pd.read_sql_query(sql_attacktype, conn)



merge1 = df_teror2.merge(df_country, how="left", left_on="COUNTRY", right_on="ID")
merge2 = merge1.merge(df_attacktype, how="left", left_on="ATTACKTYPE1", right_on="ID")

merge2.rename(columns={"NAME_x": "COUNTRY_NAME", "NAME_y": "ATTACK_NAME"}, inplace=True)
print(merge2[["COUNTRY_NAME", "ATTACK_NAME"]].head(100))


# Tohle je poměrně těžkopádné. Jednak musíme rozepsat merge po dvojicích, jednak musíme přejmenovat sloupce. Hlavně je to mimořádně neefektivní. Potřebujeme z databáze získat 3 velké tabulky, na našem počítači je postupně zmergovat, a nechat si z nich jen malý zlomek.
# 
# Tohle je typický případ, kdy bychom preferovali nechat veškerou práci na databázi.

# ## INSERT

# Je samozřejmě taky možný, ale tady se do něj pouštět nebudeme. Vyžadovalo by to přenastavit schéma aby měl každý práva zapisovat, a je trochu problém napsat to efektivně. Smyslem lekce bylo ukázat že je možné propojit Python se Snowflake (případně libovolnou jinou databází), detaily si podle potřeby každý dohledá.

# ## Zavření spojení

# Stejně jako spojení do souboru je potřeba spojení do databáze na konci zavřít.
# 
# Opět lze použít `with` blok a nechat si ho zavřít automaticky.
# ```python
# with snowflake.connector.connect(
#     user=name,
#     password=password,
#     account=ACCOUNT,
#     warehouse=WAREHOUSE,
#     database=DATABASE,
#     schema=SCHEMA,
#     role=role,
# ) as conn:
#     pass
# ```
# V rámci tohoto notebooku se to úplně nehodí, protože spojení potřebujeme používat na víc dotazů během celé lekce. Pokud ale provádíme dotazy zhruba po sobě, je vhodné `with` blok použít, stejně jako při práci se soubory. Pozor jen že navázání spojení chvíli trvá, stejně jako otevření souboru. Taky se může stát, že po mnoha opakovaných spojeních nás server na nějakou dobu zablokuje.


conn.close()
