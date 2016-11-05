import os
import datetime

# Occulus Omega btrfs revision based backup script.

# CONFIGURATION START

#exclude this path
archivePath = "/archive/"
excludePaths = []
excludePaths.append("/sys")
excludePaths.append("/proc")

# these are the systems for the script to back up.
backupSystems = []
backupSystems.append("system1.host.com")
backupSystems.append("system2.host.com")
backupSystems.append("system3.host.com")

# CONFIGURATION END

def doArchive(sysName):
    today = datetime.date.today()
    date = today.strftime('%Y-%m-%d')
    
    currentPath = archivePath + "current/" + sysName
    todayPath = archivePath + date + "/" + sysName
    
    cmd = "cp -rp --reflink " + currentPath + " " + todayPath

    print("mkdir -p " + todayPath)
    print(cmd)
    os.system("mkdir -p " + todayPath)
    os.system(cmd)

def doBackup(sysName):
    # this uses rsync to get sysPath and store in the archive under sysName
    cmd = "rsync -av "

    for path in excludePaths:
        cmd = cmd + "--exclude " + path + " "

    cmd = cmd + sysName + ":/ "
    cmd = cmd + archivePath + "current/" + sysName + "/ "

    print("mkdir -p " + archivePath + "current/" + sysName)
    print(cmd)
    os.system("mkdir -p " + archivePath + "current/" + sysName)
    os.system(cmd)
def backupList():
    for system in backupSystems:
        doBackup(system)

def archiveList():
    for system in backupSystems:
        doArchive(system)
