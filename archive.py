import os
import datetime
import config

# CONFIGURATION START

#exclude this path
archivePath = config.archivePath
excludePaths = config.excludePaths

# these are the systems for the script to back up.
backupSystems = config.backupSystems

# Occulus Omega btrfs revision based backup script.

archivePath = config.archivePath
excludePaths = config.excludePaths
backupSystems = config.backupSystems

def doArchive(sysName):
    today = datetime.date.today()
    date = today.strftime('%Y-%m-%d')
    
    currentPath = archivePath + "current/" + sysName
    todayPath = archivePath + date + "/" + sysName
    
    print("rm -rf " + todayPath)
    os.system("rm -rf " + todayPath)
    cmd = "cp -rp --reflink " + currentPath + " " + todayPath
    print(cmd)
    os.system(cmd)

def doBackup(sysName):
    # this uses rsync to get sysPath and store in the archive under sysName
    cmd = "rsync -av "

    for path in excludePaths:
        cmd = cmd + "--exclude " + path + " "

    cmd = cmd + sysName + ":/ "
    cmd = cmd + archivePath + "current/" + sysName 

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
