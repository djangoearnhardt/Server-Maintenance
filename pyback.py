import os, shutil

# map network locations
maa_13 = ('D:\\BBBack')
netserv_5 = ('B:\\EE.SQL')
# sort directory contents into list based on oldest to newest file
backup_folder = sorted(os.listdir((os.chdir(maa_13))), key=os.path.getctime)                 
# finds the newest file
backup_file = backup_folder[-1]
# copies the newest file to network location
backup_location = os.path.join(maa_13, backup_file)
shutil.copy2(backup_location, netserv_5)

# pyback.py copies local database daily backup to a network location
# shutil.copy2 includes meta data and permissions
