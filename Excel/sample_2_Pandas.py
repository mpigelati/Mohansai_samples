import pandas as pd
import xlsxwriter
#help("pandas")
#print(dir(pd))

#help(pd.read_csv)

#print(pd.ExcelWriter)
#print(pd.methos)

fd= pd.DataFrame({'Data':[10,20,30,40,50,60,70,8,]})
write=pd.ExcelWriter("Excel_chat.xlsx",engine="xlsxwriter")

fd.to_excel(write,sheet_name="sheet2")


#workbook = xlsxwriter.Workbook("Excel_chat.xlsx")
#worksheet = workbook.add_worksheet()
#workbook  = writer.book
#worksheet = writer.sheets['Sheet2']

write.close()