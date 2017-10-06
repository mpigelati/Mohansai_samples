#https://www.tutorialspoint.com/python/time_strftime.htm

import time
import datetime

#StartedAt= "2017-07-11T15:07:59.869672233Z"

tick=time.time()

print(tick)

locattime=time.localtime(tick)
print(locattime)

ldate_time=datetime.datetime.now()
print(ldate_time)

Mldate_time=datetime.datetime.now().time()

print("time",Mldate_time)

Mldate_time=datetime.datetime.now().date()
print("date",Mldate_time)

Mldate_time=datetime.datetime.now().strftime("%d-%m-%Y")
print(Mldate_time)

