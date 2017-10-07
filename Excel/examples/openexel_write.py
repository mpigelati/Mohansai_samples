import openpyxl
'''
wb = openpyxl.load_workbook("CSVFile_11kb.xlsx")

sheet_names = wb.get_sheet_names()
for name in sheet_names:
    print(name)
#shetnames=wb.get_sheet_by_name("Sheet")
sheetname=wb.get_sheet_by_name("Sheet3")
print(sheetname)

sheet = sheetname.active
sheet.title="name firstname age sex Department"
'''
wb = openpyxl.Workbook()
wb1 = wb.active

wb1.title= "sample"
for row in range(1,10):
    wb1.append(range(10))


wb.save(filename = "sample.xlsx")