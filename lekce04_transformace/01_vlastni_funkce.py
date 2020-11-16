# # Transformace

# ![transformace](transformace.png)

# ## 1. Vlastní funkce

# Příklad: funkce `round`, `len`, `random`, `open`.
#
# * Funkce je poměrně základním konceptem v Pythonu a programování vůbec.
# * Dosud jsme jich potkali spoustu, jak přímo z Pythonu nebo z nějaké knihovny (`requests`, `pandas`, ...).
# * Je možné definovat si vlastní funkce.
#
#
# * Umožňuje definovat blok kódu provádějící určitou specializovanou činnost, která se opakuje.
# * Přesné chování funkce je závislé na vstupních parametrech.
# * Vrací hodnotu jako výsledek.

# ![triangle](triangle-area.png)

# Z kodim.cz ukradneme nápad na funkci pro výpočet obsahu trojúhelníku.

# +
height1 = 3
width1 = 6
area1 = (height1 * width1) / 2
print(area1)

height2 = 4
width2 = 3
area2 = (height2 * width2) / 2
print(area2)


# -

# Pokud potřebujeme spočítat obsah mnoha trojúhelníků, začne být otravné vypisovat pořád ten samý kód dokola. Navíc při častém opisování toho samého snadno uděláme chybu.
#
# Definujeme si funkci, která v parametrech dostane rozměry trojúhelníku a jako výsledek vrátí jeho obsah.

def triangle_area(height, width):
    return (height * width) / 2


# +
area1 = triangle_area(3, 6)
print(area1)

area2 = triangle_area(4, 3)
print(area2)


# -

# Formát definice funkce je následující.
# ```
# def <nazev_funkce>(<parametry>):
#     <libovolny kod>
# ```
#
# * Názvy funkcí se řídí stejnými pravidly, jako názvy proměnných.
# * Funkce může mít libovolný počet parametrů. Pokud nemá žádné, kulaté závorky necháme prázdné (být tam ale musejí).
# * Uvnitř těla funkce (odsazené pod jejím názvem a parametry) může být libovolný kód.
# * Proměnné definované uvnitř funkce existují pouze tam, zvenčí nejsou viditelné.
# * Pokud funkce vrací nějaký výsledek, uvedeme na konci `return <vysledek>`.

# ### Součet kladných hodnot

def sum_positive(values):
    result = 0
    
    for value in values:
        if value > 0:
            result += value
            
    return result


test1 = [1, 2, 3, 4, 5]
python_sum1 = sum(test1)
my_sum1 = sum_positive(test1)
print(f"Python sum: {python_sum1}")
print(f"My sum: {my_sum1}")

test2 = [-1, 2, 3, -4, 5]
python_sum2 = sum(test2)
my_sum2 = sum_positive(test2)
print(f"Python sum: {python_sum2}")
print(f"My sum: {my_sum2}")


# ### Zápis do CSV
# Funkce bez návratové hodnoty. Pozor, je velmi zjednodušená, v praxi by se měly použít pandas nebo pythonovský modul pro práci s CSV soubory.

def write_to_csv(path, nested_list):
    f = open(path, mode="w", encoding="utf-8")
    
    for inner_list in nested_list:
        str_list = [str(v) for v in inner_list]
        f.write(",".join(str_list))
        f.write("\n")
    
    f.close()


data = [["hello", "python"], ["goodbye", "python"], [123, 456]]
write_to_csv("test.csv", data)

# !cat test.csv

# ### Převod školních známek
# Funkce mohou také zpřehlednit kód. Použijeme příklad z dřívejška s převodem známek z písmen na čísla.

grades = ["A", "A", "B", "A", "C", "D", "E", "C", "B", "A", "C"]

converted1 = [grade.replace("A", "1").replace("B", "2").replace("C", "3").replace("D", "4").replace("E", "5")
              for grade in grades]
print(converted1)


def convert_grade(grade):
    return grade.replace("A", "1").replace("B", "2").replace("C", "3").replace("D", "4").replace("E", "5")


converted2 = [convert_grade(grade) for grade in grades]
print(converted2)


def convert_grade_better(grade):
    if grade == "A":
        return "1"
    elif grade == "B":
        return "2"
    elif grade == "C":
        return "3"
    elif grade == "D":
        return "4"
    else:
        return "5"


converted3 = [convert_grade_better(grade) for grade in grades]
print(converted3)
