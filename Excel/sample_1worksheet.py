import workbook
import xlsxwriter

#orkbook1=xlsxwriter.Workbook("temp1.xlsx")

#workbook5=workbook1.add_worksheet()
#workbook4=workbook1.add_worksheet()

#workbook5.write("A1",1234)

workbook   = xlsxwriter.Workbook('filename.xlsx')

worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()

worksheet1.write('A1', 123)

workbook.close()
