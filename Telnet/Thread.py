import _thread

print("start thread")


def Fun_start(i,data):
    print(i, data)

i=0
date="mohansai"

try:
    _thread.start_new_thread(Fun_start,(i, date))
except:
    print("failed to create theread")
