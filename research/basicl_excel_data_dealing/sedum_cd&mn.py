import openpyxl as op

filename = 'X.xlsx'
wb = op.load_workbook(filename)
sheet = wb.active

ecotype