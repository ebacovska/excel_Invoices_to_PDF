import pathlib
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("/home/elen/Projekty/Udemy/The Python Mega Course- Learn Python in 40 Days with 18 Apps/excel_Invoices_to_PDF/data_file/*.xlsx")


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    
    pdf = FPDF(orientation = "P", unit = "mm", format = "A4")
    pdf.add_page()
    
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]
    
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)
    
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date {date}")
    
    pdf.output(f"excel_Invoices_to_PDF/PDFs/{filename}.pdf")
