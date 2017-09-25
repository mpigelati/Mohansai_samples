#import pandas
#help(pandas)

import pandas as pd

#fd= pd.DataFrame({"name":["Bhagavan","chandana","saketh","vachan","Narasimha","Lavanya","Deeru","likith"]})
#write =pd.ExcelWriter("sample.xlsx",engine="xlsxwriter")

#fd.to_excel(write,sheet_name="sheet4")

fd= pd.DataFrame({"data":[42,35,14,9,40,32,8,9,8,]})

write =pd.ExcelWriter("sample.xlsx",engine="xlsxwriter")

fd.to_excel(write,sheet_name="sheet4")

write.close()