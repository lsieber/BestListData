from src.sa2tvustat.findTVUAthletes import findAllTVUAthletes, saveAthleteIdsCSV
import os
from src.sa.bl.getAllAthleteResults import getAllAthletesPerfromances
from src.sa2tvustat.dataUploaderHelper import uploadPerformanceClass
from src.sa.bl import storeSaData


def addPerformancesToTvustat(url, performances):
    for p in performances:
        print(p.printDetails())
        uploadPerformanceClass(url, p, 1)


if __name__ == '__main__':
    year = 2020
    os.chdir('C:/Users/lukas/Documents/TVU/tvustat/sa2tvu/%s' % year)
    print("working in directory: " + os.getcwd())
    
    urlLocal = "http://localhost/tvustat/public/insertPerformanceWithCompetition.php"
    urlWeb = "http://tvulive.bplaced.net/tvustat/public/insertPerformanceWithCompetition.php"
    url = urlLocal
        
    downloadFromSa = False
    if downloadFromSa:
        athletes = findAllTVUAthletes(year)
        saveAthleteIdsCSV(athletes, "athleteIDs.csv")
        storeSaData.storeAthletes("athletes.json", athletes)
         
        performances = getAllAthletesPerfromances(athletes, year)
        storeSaData.storePerformances("performances.json", performances)

    athletesDict = {a.id : a for a in storeSaData.loadAthletes("athletes.json")}
    jsonPerf = storeSaData.loadPerformances("performances.json", athletesDict)
    
    addPerformancesToTvustat(url, jsonPerf)
    
