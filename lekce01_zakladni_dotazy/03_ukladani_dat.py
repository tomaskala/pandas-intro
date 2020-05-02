import pandas

mesta = pandas.read_csv("mesta.csv", index_col="mesto", encoding="utf-8")

# ## 3. Ukládání dat

mesta.to_csv("data.csv")

mesta.to_html("data.html")

mesta.to_excel("data.xls")

mesta.to_json("data.json", indent=4)
