import sys

sys.path.append("/home/mohansai/python/Mohansai_samples/class/out_side_of_class")
import adb
from adb import myadb
print(adb.hellow())
#here  myadb is class object
adb = myadb()
#adb=adb.myadb()
adb._data_()