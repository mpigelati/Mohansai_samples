import pandas as pd

#fd= pd.read_csv("sampe.csv")
fd=pd.read_csv("sample.csv",header=1,names=["Name","Fullname","Uid","Gid","Phone", "H_Phone","Address","Email","Enabled"])
print(fd)


