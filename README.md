# Pandas Intro

Úvod do knihovny [Pandas](https://pandas.pydata.org/). Založeno na materiálech z [kodim.cz](http://kodim.cz/kurzy/python-data/).

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

### Lekce 2 - agregace

#### Funkce nad Pandas
* `concat([df1, df2, df3, ...])`
    * Spojí daný seznam DataFrames pod sebe.
    * Defaultně naskládá za sebe i jejich indexy, čímž se tam typicky objeví duplikáty.
    * `concat([df1, df2, df3, ...], ignore_index=True)` udělá to samé, ale index vytvoří nový číselný.
* `merge(df1, df2)`
    * Ekvivalent `JOIN` v SQL, defaultně provádí `INNER JOIN` přes všechny sloupce, které mají v obou DataFrames stejný název.
    * Možno dodat parametr `how=typ_joinu`, kde `typ_joinu` je jeden z `"left"`, `"right"`, `"outer"`, `"inner"`.
    * Také je možné dodat parametr `on=x`, kde `x` je buď název sloupce (je-li 1), nebo seznam názvů sloupců, podle kterých se má dělat `JOIN`.

#### Funkce nad DataFrame
* `dropna()`
    * Zahodí řádky s chybějícími hodnotami.
    * Zkrácená verze `dropna(axis="index")`.
* `dropna(axis="columns")`
    * Zahodí sloupce s chybějícími hodnotami.
* `fillna(x)`
    * Nahradí chybějící hodnoty hodnotou `x`.
* `rename(columns=slovnik)`
    * Přejmenuje sloupce v DataFrame pomocí slovníku, jehož klíče jsou staré názvy a jim odpovídající hodnoty jsou nové názvy. Pokud nějaký sloupec ve slovníku neuvedeme, jeho název se nezmění.
* `groupby(x)`
    * Seskupí hodnoty v DataFrame podle sloupce/seznamu sloupců `x`.
    * Vrací `DataFrameGroupBy object`.
* `sort_values(by=x)` (bylo navíc kvůli dotazu)
    * Seřadí řádky podle sloupce `x`, respektive seznamu sloupců `x`.
    * Když dáme seznam sloupců, řadí nejprve podle prvního, pak podle druhého, atd.
    * Lze volat i na Series.
    * Bere parametr `ascending` (defaultně `True`), kterým ovládáme, jestli se má řadit vzestupně (`True`) nebo sestupně (`False`).
    

#### Funkce nad DataFrameGroupBy object
* `count()`
    * Četnost hodnot, zadnedbává chybející hodnoty.
* `sum()`
    * Součet hodnot.
* `max()`
    * Maximální hodnota.
* `min()`
    * Minimální hodnota.
* `first()`
    * První hodnota.
* `last()`
    * Poslední hodnota.
* `mean()`
    * Průměr z hodnot.
* `median()`
    * Medián z hodnot.
* `var()`
    * Rozptyl hodnot.
* `std()`
    * Směrodatná odchylka hodnot.
* `all()`
    * True, pokud jsou všechny hodnoty True.
* `any()`
    * True, pokud je alespoň jedna z hodnot True.
* `agg([fun1, fun2, fun3, ...])`
    * Aplikuje seznam agregačních funkcí daných jako názvy funkcí vyjmenovaných výše.
    * Např. tedy `df.agg(["mean", "max", "min", "std"])`.

#### Funkce nad Series
* `isnull()`
    * Vrátí `True` na pozicích kde chybí hodnota a `False` na pozicích kde hodnota nechybí.
    * Možno volat také nad DataFrame, pak vrací celý DataFrame takovýchto pravdivostních hodnot.
* `astype(int)`
    * Vrátí kopii Series převedenou na celočíselný typ.

### Lekce 3 - transformace

#### Tvorba vlastních funkcí
Funkce, která nebere žádné argumenty a nevrací žádný výsledek. Aby měla smysl, měla by mít nějaký tzv. vedlejší efekt, tedy něco vypisovat na obrazovku, do souboru, přes síť a podobně.
```
def <nazev_funkce>():
    <kod>
```

Funkce, která nebere žádné argumenty a vrací výsledek. Může provést nějaký výpočet a vrátit jeho výsledek, ale nelze ji parametrizovat podle vstupu.
```
def <nazev_funkce>():
    <kod>
    return <vysledek>
```

Funkce, která bere argumenty a nevrací žádný výsledek. Podobné jako 1. případ, ale lze ji parametrizovat podle vstupu.
```
def <nazev_funkce>(<arg1>, <arg2>, ..., <argN>):
    <kod>
```

Funkce, která bere argumenty a vrací výsledek. Kombinace předchozích dvou případů.
```
def <nazev_funkce>(<arg1>, <arg2>, ..., <argN>):
    <kod>
    return <vysledek>
```

#### Funkce nad Pandas
* `to_numeric(series)`
    * Převede danou Series do číselného typu. Je to čistší než volat `astype()`, protože tím jasně dáváme najevo, že očekáváme čísla. Navíc můžeme definovat co se má stát s hodnotami, které se nepovedlo převést.

#### Funkce nad Series
* `str`
    * Obsahuje-li Series textové řetězce, umožňuje s ní pracovat jako s klasickým textem, tedy získat podřetězce, převádět velikost písmen, apod.
    * `str.replace(what, with)`
        * Nahradí všechny výskyty řetězce `what` řetězcem `with`.
* `apply(function)`
    * Vezme danou funkci, a aplikuje ji postupně na každý prvek Series. Vrací novou Series, jejíž hodnoty jsou výsledky volání dané funkce.
    * Podobné chroustání seznamu.
* `agg(function)`
    * Už jsme potkali v minulé lekci, kde jsme funkci `agg` používali pro aplikaci víc agregačních funkcí najednou. Tehdy jsme jako vstup dávali seznam názvů (ve stringu) funkcí, které chceme aplikovat. Ty funkce ale musely existovat v pandas, proto jsme byli relativně omezeni (zas tak moc ne, pandas jich má dost).
    * V této lekci jsme viděli, že funkci `agg` lze dát také námi definovanou agregační funkci. Tato námi definovaná funkce očekává jako vstup Series, jako výstup vrací číslo.
    * Lze volat též nad DataFrameGroupBy object.
