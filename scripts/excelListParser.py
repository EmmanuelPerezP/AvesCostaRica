import pandas as pd
import os

script_directory = os.path.split(os.path.abspath(__file__))[0]
print(script_directory)
abs_filename = os.path.join(script_directory, "lista-julio-18.xlsx")
print(abs_filename)



# xls = pd.ExcelFile("../lista-julio-18.xlsx")
xls = pd.ExcelFile(abs_filename)

sheetX = xls.parse(0) #0 is the sheet number

print("Column headings:")
print(sheetX.columns)
# var1 = sheetX['']


# print(var1[1]) #1 is the row number...