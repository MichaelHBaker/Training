import pandas as pd 
import os
import xlrd

filename = str(os.getcwd()).replace("\\","/")+"/test.xlsx"
file = filename
xl = pd.ExcelFile(file)

print(xl.sheet_names)