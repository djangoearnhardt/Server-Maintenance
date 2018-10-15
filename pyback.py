import os, shutil

maa_11 = ('D:\\BBBack')
netserv_5 = ('B:\\EE.SQL')
backup_folder = os.listdir(maa_11)                    
backup_file = backup_folder[-1]
backup_location = os.path.join(maa_11, backup_file)
shutil.copy2(backup_location, netserv_5)

# pyback.py copies Financial Edge's daily backup to Netserv5
# shutil.copy2 includes meta data and permissions
