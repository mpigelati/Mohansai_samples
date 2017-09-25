import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
fp=pd.read_excel("excel-comp-data.xlsx")

#=============================================
#print(dp.head())

#fp["total"] = fp["Jan"]
#fp["total"] = dp["Jan"] + dp["Feb"] + dp["Mar"]
#print(fp.head())
#=========================================

#print(fp.columns)

#print(fp["street"])

#for i in fp.index:
    #print(fp["street"][i])
#    print(fp["city"][i])
#=======================================
#list=fp["city"]
#print(list[0])
#=====================================
fd=pd.read_excel("excel-comp-data.xlsx")

city=fd["city"]
print(city)

#print("state"[%s],"city"[%s]%)
#state=fd["state"]
#print(state)