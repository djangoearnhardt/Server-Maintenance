# ServerMaintenance
I wanted to incorporate some automation on three servers where daily backups are created. They are financial, donor, and keycard databases. The backups are moved off the local machine incase it crashes and we have another place to recover them from. I use Task Scheduler on the three servers to schedule these scripts to run at seperate times of the morning. 

PyBack - Script for moving backups from local to network drive

PyClean - Maintains the size of backup directories, to prevent backups from clogging up storage
