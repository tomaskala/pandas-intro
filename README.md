# Pandas Intro

Úvod do knihovny [Pandas](https://pandas.pydata.org/).

## Souhrn probrané látky

### Lekce 1 - základní dotazy

#### Funkce nad Pandas
* `pandas.read_csv()`, `pandas.read_excel()`, ...
    * Načte soubor z CSV, Excelu, ... do DataFrame.
* `pandas.concat()` (bylo navíc kvůli dotazu)
    * `pandas.concat([df1, df2, ...], axis=n)` spojí dohromady daný seznam DatFrames, a to:
        * pod sebe, pro `n = 0`,
        * vedle sebe, pro `n = 1`.

#### Funkce nad DataFrame
* `info()`
    * Vrátí string obsahující souhrnné informace o DataFrame (názvy sloupců, velikost, datové typy).
* `shape`
    * Vrátí `(pocet_radku, pocet_sloupcu)`.
* `columns`
    * Vrátí názvy sloupců jako Pandas sérii (`Series`).
    * `list(dataframe)` vrátí názvy sloupců v seznamu.
* `describe()`
    * Základní statistické údaje o *číselných* sloupcích -- minimum, maximum, průměr, medián, ...
    
* `head()`
    * Vrátí prvních pár (defaultně 5) řádků DataFrame.
    * `head(n)` vrátí prvních `n` řádků.

* `loc`
    * Výběr řádků/sloupců/obojího pomocí názvu.
    * `df.loc[radky]` vybere dané řádky a všechny sloupce.
    * `df.loc[:, sloupce]` vybere všechny řádky a dané sloupce.
        * Možno zkrátit na `df[sloupce]`. Pro výběr řádků podle jmen taková zkratka není.
    * `df.loc[radky, sloupce]` vybere dané řádky i sloupce.
    * Výběr řádků/sloupců je vždý mozný pomocí názvu/seznamu/rozsahu, výběr řádků navíc ještě jako podmínka (viz sekce 5. Dotazy jako v SQL v Jupyter notebooku k 1. Pandas lekci).
* `iloc`
    * Obdobný jako `loc`, ale výběr pomocí číselných indexů začínajících od 0.
* `to_excel(cesta)`, `to_csv(cesta)`, ...
    * Uloží DataFrame do Excelu, CSV, ... na dané cestě.
* `set_index(nazev_sloupce)`
    * Sloupec `nazev_sloupce` smaže z části sloupců a vytvoří z něj index (názvy řádků).
* `reset_index()`
    * Dosavadní index přesune mezi sloupce a vytvoří nový číselný začínající od 0.
    * `reset_index(drop=True)` udělá to samé, ale starý index úplně zahodí, nepřesune ho do sloupců.
* `index`
    * Získá index daného DataFrame.
