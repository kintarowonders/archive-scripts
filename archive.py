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
sysAliases = config.sysAliases

def doArchive(sysName):
    today = datetime.date.today()
    date = today.strftime('%Y-%m-%d')
    
    currentPath = archivePath + "current/" + sysName
    todayPath = archivePath + date + "/" + sysName
    
    try:
        os.mkdir(archivePath + date)
    except FileExistsError:
        print("Archive path already exists, possibly already done archival.")
    cmd = "cp -vrp --reflink " + currentPath + "* " + todayPath
    print(cmd)
    os.system(cmd)

def getPort(sysName):
    a = sysName.split('%%')
    
    if (len(a) == 2):
        try:
            port = int(a[1])
        except ValueError:
            return 0
        return int(a[1])
    else:
        return 0

def getAlias(sysName):
    if sysName in sysAliases:
        return sysAliases[sysName]
    else:
        return sysName

def doBackup(sysName):
    port = getPort(sysName)
    sysName = getAlias(sysName)
    
    if (port == 0):
        port = 22

    cmd = "rsync -av -e \"ssh -p " + str(port) + "\" "

    for path in excludePaths:
        cmd = cmd + "--exclude " + path + " "

    cmd = cmd + sysName + ":/ "
    cmd = cmd + archivePath + "current/" + sysName 

    print("mkdir -p " + archivePath + "current/" + sysName)
    print(cmd)
    #os.system("mkdir -p " + archivePath + "current/" + sysName)
    #os.system(cmd)

def backupList():
    for system in backupSystems:
        doBackup(system)

def archiveList():
    for system in backupSystems:
        doArchive(system)
