import pandas as pd
import glob

filepaths = glob.glob("/home/elen/Projekty/Udemy/The Python Mega Course- Learn Python in 40 Days with 18 Apps/excel_Invoices_to_PDF/data_file/*.xlsx")


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    
