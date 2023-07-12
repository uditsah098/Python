#############################
# Author:UDIT SAH           #
# To check the disk info.   #
#############################
import os
import shutil

total,used,free=shutil.disk_usage("/")
print("Total disk= "+str(total//(2**30))+" GB")
print("Used disk= "+str(used//(2**30))+" GB")
print("Avilable disk= "+str(free//(2**30))+" GB")
