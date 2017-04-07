# the path where archives are kept
archivePath = "/archive/"

# the paths which are excluded from backups to current
excludePaths = []
excludePaths.append("/sys")
excludePaths.append("/proc")
excludePaths.append("/proc")
excludePaths.append("/run")

global archivePath
global excludePaths

# these are the systems for the script to back up.
backupSystems = []
backupSystems.append("system1.host.com")
backupSystems.append("system2.host.com")
backupSystems.append("system3.host.com")

global backupSystems

# how many days to archive for (integer)
archiveForDays = 14
global archiveForDays
