# ServerMaintenance
I wanted to incorporate some automation on three servers where daily backups are created. The backup files are from financial, donor records, and keycard access databases. The backups are moved off the local machines incase they crash, and we have another place to recover them from. I use Task Scheduler on the three servers to schedule these scripts to run at seperate times of the morning. 

PyBack - Script for moving backups from local to network drive

PyClean - Maintains the size of backup directories, to prevent backups from clogging up storage
