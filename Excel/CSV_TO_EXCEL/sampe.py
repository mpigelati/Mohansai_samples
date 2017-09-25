import pandas as pd

#fd= pd.read_csv("sample.csv")
#fd=pd.read_csv("sample.csv",header=1,names=["Name","Fullname","Uid","Gid","Phone", "H_Phone","Address","Email","Enabled"])
#fd= pd.read_csv("sample.csv",nrows=3)# only it will pring 3 rows from file
#fd= pd.read_csv("sample.csv",nrows=2,na_values={
 #                                               ["notavailabel","n.a","NaN"])}
fd=pd.read_csv("sample.csv",header=1,names=["Name","Fullname","Uid","Gid","Phone", "H_Phone","Address","Email","Enabled"],nrows=3,na_values={"H+Phone":["not available","n.a","enable"]}  )

print(fd.columns)

