import os
import sys
import datetime
import config

global archivePath
global archiveForDays

archivePath = config.archivePath
archiveForDays = config.archiveForDays

def getDestruDirList():
    # This method creates a list of files for deletion.
    
    archiveList = os.listdir(archivePath) #get list of archive directorires
    deletionList = []                     #create list for deletion

    for dateStr in archiveList:
        skip = False
        if (not dateStr == "current"):
            dateVar = datetime.datetime.strptime(dateStr, "%Y-%m-%d")
            if dateVar.date() < datetime.datetime.now().date() - datetime.timedelta(days=archiveForDays):
                deletionList.append(archivePath + dateStr) #add full pathname to deletion list
                print("Revision " + dateVar.strftime("%d-%m-%Y") + " to be deleted.")

    return deletionList 
