# # Databáze

# V této lekci si ukážeme, jak se dá z Pandas připojit k databázi. To nám umožní psát v rámci Pythonu SQL dotazy a jako výsledky dostávat dataframes. Ukážeme si pár příkladů a porovnáme rozdíly mezi zpracováním dat v databázi a v Pandas.
# 
# Lekce předpokládá, že máte nainstalovaný Snowflake connector a funguje vám připojení k databázi. Pokud nemáte, využijte přiložený [skript](check_db.py). Spustíte jako `python check_db.py --name '<vas-snowflake-login>' --password '<vase-snowflake-heslo>'` včetně těch jednoduchých uvozovek. V mém případě tedy `python check_db --name 'CZECHITA_KALAT' --password '12345'`. Skript zkontroluje jestli máte nainstalovaný Snowflake connector, správně zadané heslo a jestli funguje připojení. Pokud ne, vypíše krátký komentář a chybu.

# Než se připojíme k databázi, ukážeme si nějakou další práci s textovými řetězci, která se nám bude hodit při psaní SQL dotazů.

# ## 1. Víceřádkové stringy a další formátování

# ### Víceřádkové stringy

# SQL dotazy se v Pythonu píšou jako obyčejné stringy. Jupyter to neumí, ale chytřejší programy poznají že je ve stringu SQL, a zvýrazní nám jeho syntaxi.
# 
# Pro snazší čitelnost je, stejně jako v klasickém SQL, zvykem psát dotazy rozdělené do více řádků. Začneme tedy ukázkou, jak psát v Pythonu víceřádkové stringy.

# Pokud ukončíme řádek uprostřed obyčejného stringu, chápe to Python jako oddělení dvou příkazů, a začne si stěžovat na neukončené uvozovky.


tohle_nepujde = "SELECT sloupec
FROM tabulka"

print(tohle_nepujde)


# Můžeme tam sice přidat znak `\n` jako nový řádek, ale ten funguje jen po vypsání na obrazovku nebo do souboru. Čitelnosti kódu to nijak nepomůže.


tohle_neni_citelne = "SELECT sloupec\nFROM tabulka"

print(tohle_neni_citelne)


# Python umožňuje začít (a ukončit) string třemi uvozovkami. Takový string pak chápe jako víceřádkový.


tohle_je_ok = """
SELECT sloupec
FROM tabulka
"""

print(tohle_je_ok)


# Takový string dokonce zachovává odsazení.


odsazeny_string = """
SELECT sloupec1,
       sloupec2,
FROM tabulka
WHERE sloupec3 IN (
    SELECT sloupec4
    FROM tabulka2
)
"""

print(odsazeny_string)


# Občas si lidé myslí, že tři uvozovky znamenají víceřádkový komentář. To ale není pravda, Python žádné víceřádkové komentáře nemá.


"""
Zde není komentář.

Zde už vůbec ne.
"""


# Jak vidíme z výstupu Jupyteru, Python vytvořil víceřádkový string. Jen se neuložil do žádné proměnné a tak hned zanikl. Narozdíl od komentářů (které se při spuštění programu přeskakují) ale Python každý víceřádkový string vytvoří, což stojí nějakou práci navíc.
# 
# Navíc je možné v rámci takového (f-)stringu spustit libovolný kód, což by v komentáři určitě jít nemělo. Není to speciální vlastnost víceřádkových stringů, totéž lze provést i v klasickém f-stringu. Jen to ukazuje rozdíl oproti komentářům.


f"""
Zde není komentář.

Zkusíme dělit nulou: {1 / 0}.
"""


# ### Další způsob formátování stringů

# Pro formátování stringů jsme si už dříve ukázali f-stringy. Ty nám umožňují do stringu dodat hodnotu libovolného Pythonovského výrazu. Ačkoliv Python umí víc způsobů, f-stringy se používají nejčastěji, protože jsou nejčitelnější a nejrychlejší.
# 
# Jejich nevýhodou ale je, že nemůžeme stejný string využít víckrát s různými hodnotami. Právě to se nám někdy hodí při psaní modulárních SQL dotazů.

# Dejme tomu, že máme tabulku studentů.

# <table>
#     <tr><th>Jméno</th><th>Bydliště</th><th>Studijní obor</th></tr>
#     <tr><td>František Novák</td><td>Praha</td><td>Historie</td></tr>
#     <tr><td>Josef Krátký</td><td>Litomyšl</td><td>Matematika</td></tr>
#     <tr><td>Petr Švec</td><td>Olomouc</td><td>Alchymie</td></tr>
#     <tr><td>David Kovář</td><td>Znojmo</td><td>Hudba</td></tr>
#     <tr><td>Prokop Novotný</td><td>Praha</td><td>Tanec</td></tr>
#     <tr><td>Marek Černý</td><td>Plzeň</td><td>Medicína</td></tr>
# </table>

# Podobně máme tabulku profesorů.

# <table>
#     <tr><th>Jméno</th><th>Bydliště</th><th>Vydaných článků</th></tr>
#     <tr><td>Jiří Volf</td><td>Brno</td><td>1</td></tr>
#     <tr><td>Jan Kulhavý</td><td>Praha</td><td>40</td></tr>
#     <tr><td>Michal Horák</td><td>Ostrava</td><td>3</td></tr>
#     <tr><td>Ondřej Veselý</td><td>Plzeň</td><td>18</td></tr>
# </table>

# Chceme vybrat studenty i profesory, kteří žijí v Praze. V obou případech bude dotaz podobný.


studenti_praha = """
SELECT jmeno
FROM studenti
WHERE bydliste = 'Praha'
"""

profesori_praha = """
SELECT jmeno
FROM profesori
WHERE bydliste = 'Praha'
"""


# Protože se oba dotazy liší jen názvem tabulky, bylo by mnohem hezčí napsat si obecný dotaz pro výběr jmen s bydlištěm v Praze, a podle potřeby do něj doplnit název tabulky.


bydliste_praha = """
SELECT jmeno
FROM {tabulka}
WHERE bydliste = 'Praha'
"""



print(bydliste_praha.format(tabulka="studenti"))



print(bydliste_praha.format(tabulka="profesori"))


# Můžeme jít ještě dál, a i místo bydliště nechat jako parametr. Jen pozor na jednoduché uvozovky okolo hodnoty.


jmeno_podle_bydliste = """
SELECT jmeno
FROM {tabulka}
WHERE bydliste = '{bydliste}'
"""



print(jmeno_podle_bydliste.format(tabulka="studenti", bydliste="Brno"))
