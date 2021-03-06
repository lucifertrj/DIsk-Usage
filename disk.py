import shutil
import time
import matplotlib.pyplot as plt

print('*'*40)
print('Disk usage Status')
print('*'*40)
time.sleep(1.5)
disk=shutil.disk_usage('/') #disk variable stores the disk usage data in it
print(f'Usage: \n Total Disk Space: {disk.total} \n Total Disk Used: {disk.used} \n Total Free space:{disk.free}')
time.sleep(1.2)
if disk.used>(disk.total*0.5):
    print('Warning: You have used more the 50% of disk')
else:
    print('Used storage is less than 50% of total disk')
    
current_percent=str((disk.free/disk.total)*100)
print('Available Percentage of Free disk: ',current_percent[0:6],'%')
min_disk_usage=disk.total*0.25
time.sleep(1.2)
if min_disk_usage>disk.free:
    print('Warning:Not enough free space, just delete some folders')
else:
    print('You have enough free space, so store whatever you want')

disk_graph = plt.plot(disk.total,disk.used,disk.free)
print(disk_graph)
