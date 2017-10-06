#http://www.pythonforbeginners.com/basics/python-datetime-time-examples

StartedAt= "2017-07-11T15:07:59.869672233Z"

import datetime
import time
import calendar


ticks= time.time()
print(datetime.time)
print(ticks)
#print(datetime.time(ticks))

print(time.localtime(ticks))


localtime=time.asctime(time.localtime(ticks))
print(localtime)

print(calendar.month(2018,1))

print(time.asctime(time.localtime(ticks)))

print(time.clock())
print(time.time())

print(time.timezone)

#print(calendar.leapdays())

print(datetime.datetime.now())

