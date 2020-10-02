from src.sa2tvustat.findTVUAthletes import findAllTVUAthletes, saveAthleteIdsCSV
import os
from src.sa.bl.getAllAthleteResults import getAllAthletesPerfromances
from src.sa2tvustat.dataUploaderHelper import uploadPerformanceClass,\
    checkAthleteExists
from src.sa.bl import storeSaData
from src.sa2tvustat import athlete2tvustat
from src.sa2tvustat.athlete2tvustat import confirm


def addPerformancesToTvustat(url, performances):
    for p in performances:
        p.printDetails()
        uploadPerformanceClass(url, p, 1)


if __name__ == '__main__':
    year = 2020
    os.chdir('C:/Users/lukas/Documents/TVU/tvustat/sa2tvu/%s' % year)
    print("working in directory: " + os.getcwd())
    
    urlAthleteCheck = "http://tvulive.bplaced.net/tvustat/public/existing_entries.php"
    urlLocalCheck = "http://localhost/tvustat/public/existing_entries.php"
    urlCheckAthlete = urlAthleteCheck
 
    urlAthleteInsertationLocal = "http://localhost/tvustat/public/insertToDB.php"
    urlAthleteInsertationWeb = "http://tvulive.bplaced.net/tvustat/public/insertToDB.php"
    urlathleteInsert = urlAthleteInsertationWeb
    
    urlLocal = "http://localhost/tvustat/public/insertPerformanceWithCompetition.php"
    urlWeb = "http://tvulive.bplaced.net/tvustat/public/insertPerformanceWithCompetition.php"
    url = urlWeb
        
    downloadFromSa = False
    if downloadFromSa:
        athletes = findAllTVUAthletes(year)
        saveAthleteIdsCSV(athletes, "athleteIDs.csv")
        storeSaData.storeAthletes("athletes.json", athletes)
         
        performances = getAllAthletesPerfromances(athletes, year)
        storeSaData.storePerformances("performances.json", performances)

    
    athletesDict = {a.id : a for a in storeSaData.loadAthletes("athletes.json")}
    for athlete in athletesDict.values():
        if not checkAthleteExists(urlCheckAthlete, athlete.name, athlete.birthDate):
            if confirm("Insert %s, Yob: %s, %s To Database?" % (athlete.name, athlete.birthYear, athlete.gender)):
                athlete2tvustat.athlete2tvustatClass(urlathleteInsert, athlete, year+5, None, athlete.id)
   
    
    jsonPerf = storeSaData.loadPerformances("performances.json", athletesDict)
    
    addPerformancesToTvustat(url, jsonPerf)
    
