# the path where archives are kept
global archivePath
archivePath = "/archive/"

# the paths which are excluded from backups to current
global excludePaths
excludePaths = []
excludePaths.append("/sys")
excludePaths.append("/proc")
excludePaths.append("/proc")
excludePaths.append("/run")

# these are the systems for the script to back up.
global backupSystems
backupSystems = []
backupSystems.append("system1.host.com")
backupSystems.append("system2.host.com")
backupSystems.append("system3.host.com")

# how many days to archive for (integer)
global archiveForDays
archiveForDays = 14

global sysAliases
sysAliases = {
                'localhost%%2022': 'localserver',
                'localhost%%3022': 'otherserver'
             }
