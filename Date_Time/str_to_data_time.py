import datetime

StartedAt= "2017-07-11T15:07:59.869672233Z"


def convert_date_time(y,m,d,h,mi,s):

    print(y,m,d,h,mi,s)
    date_time = datetime.datetime(int(y),int(m),int(d),int(h),int(mi),int(s))
    print(date_time)
    print(type(date_time))
    date_time = datetime.datetime(int(d),int(m),int(y),int(h),int(mi),int(s))
    print(date_time)
    string = d-m-y


def C_dat_time(str):
    #print(str)
    date,time=str.split("T")
    #print("time",time)
    time=time.split(".")[0]
    #print("time", time)
    #print("date",date)
    yy,mm,dd=date.split("-")
    #print(yy,mm,dd)
    hh,mm,ss=time.split(":")
    #print(hh,mm,ss)
    convert_date_time(yy,mm,dd,hh,mm,ss)

#if __name__ == '__main__':
if __name__ =='__main__' :
    C_dat_time(StartedAt)