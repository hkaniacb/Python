import openpyxl
from datetime import date
import os.path as op

name_workbook = 'sample.xlsx'
name_sheet = 'Ceneo'

print("Czy istnieje pilk: "+op.exists(name_workbook))

if op.exists(name_workbook):
    print('Exist workbook ' + name_workbook)
    wb = openpyxl.load_workbook(name_workbook)#   Workbook("sample.xlsx")
else:
    print('Create workbook ' + name_book)
    wb = openpyxl.Workbook()

#Sprawdza czy istanieje arkusz i tworzy jeśli nei
if name_sheet in wb.sheetnames:
    print('Exist sheet ' + name_sheet)
    ws =  wb[name_sheet]
else:
    print('Create Sheet '+name_sheet)
    ws = wb.create_sheet(name_sheet, 0)

#Dodaje wiersz
ws.append([date.today(),"Hello"])

#Zapisuje Workbook
wb.save(name_workbook)
