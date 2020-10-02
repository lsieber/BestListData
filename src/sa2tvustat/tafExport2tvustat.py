from builtins import set
import datetime
import os

from src.elmt.Athlete import Athlete
from src.elmt.Competition import Competition
from src.elmt.Performance import Performance
from src.io.exportCSV import exportCSV
from src.io.exportPerformancesToCsv import exportPerformancesToCsv
from src.sa.config.disziplins import getDisziplinByTAF
from src.sa2tvustat import athlete2tvustat
from src.sa2tvustat.athlete2tvustat import confirm
from src.sa2tvustat.dataUploaderHelper import checkAthleteExists, \
    uploadPerformanceClass

dictUBSKidsCup = {"60M": "60", "WEZ": "Weit Z", "BAL": "BALL200"}
tvuID = "1.BE.0159"
tvuName = "TV Unterseen"

 
def uploadResults(url, competition, resultsFile, source, urlAthleteCheck):
     
    table = []
    with open(resultsFile, mode="r") as f:
        for line in f: 
            table.append(line.split(";"))
     
    firstNameId = table[0].index("FirstName")
    lastNameId = table[0].index("LastName")
    birthYearId = table[0].index("Yob")
    clubCodeId = table[0].index("ClubCode")
    clubNameId = table[0].index("ClubName")
    genderId = table[0].index("Gender")
    disziplinTafId = table[0].index("Event")
    performanceId = table[0].index("Result")
    windId = table[0].index("Wind")
     
    print(firstNameId)
    notinsertedPerformances = []
    for l in table[1:20000]:
        if l[clubCodeId] == tvuID or l[clubNameId] == tvuName:
            fullName = l[firstNameId] + " " + l[lastNameId]
            birthYear = l[birthYearId]
            disziplin = getDisziplinByTAF(l[disziplinTafId])
            detail = "" if disziplin.multiple == None else getDetailFromTable(disziplin.multiple, table, l[firstNameId], l[lastNameId], performanceId);
            perf = l[performanceId].replace(".", "").replace(",", ".")
            if perf != 0 and perf != "0" and perf != None and perf != "":
                athlete = Athlete(None, fullName, l[genderId], birthYear, tvuName);
                p = Performance(perf, athlete, competition, disziplin, "", l[windId], detail)
             
                if checkAthleteExists(urlAthleteCheck, fullName, birthYear):
    
                    print("{} {} {} {} {}".format(p.athlete.name, p.disziplin.name, p.result, p.competition.date, p.wind))
                    uploadPerformanceClass(url, p, source)
                else:
                    notinsertedPerformances.append(p)
    return notinsertedPerformances
    
    
def getDetailFromTable(disziplins, table, firstName, lastName, pId):
    detail = [];
    for d in disziplins:
        for l in table:
            if firstName in l and lastName in l and d in l:
                detail.append(dictUBSKidsCup[d] + " " + l[pId].replace(".", "").replace(",", ".")) 
    return "/".join(detail);
     
     
def findAthletesToInsert(resultsFile, urlAthleteCheck):
    table = []
    with open(resultsFile, mode="r") as f:
        for line in f: 
            table.append(line.split(";"))
     
    firstNameId = table[0].index("FirstName")
    lastNameId = table[0].index("LastName")
    birthYearId = table[0].index("Yob")
    clubCodeId = table[0].index("ClubCode")
    clubNameId = table[0].index("ClubName")
    genderId = table[0].index("Gender")
    notExistingAthletes = set()
    existingAthletes = set()
    for l in table[1:10000]:
        if l[clubCodeId] == tvuID or l[clubNameId] == tvuName:
            fullName = l[firstNameId] + " " + l[lastNameId] 
            birthYear = l[birthYearId]
            if not (fullName, birthYear) in notExistingAthletes and not (fullName, birthYear) in existingAthletes :
                if not checkAthleteExists(urlAthleteCheck, fullName, birthYear):
                    notExistingAthletes.add((fullName, birthYear, l[genderId]))
                else:
                    existingAthletes.add((fullName, birthYear))
    exportCSV(notExistingAthletes, "notExistingAthletes{}.csv".format(datetime.datetime.now().strftime("%Y%m%d%H%M")))
    if len(notExistingAthletes) == 0:
        print("\n\nReady For Insertation. All Athletes are in the DB\n\n")
    return notExistingAthletes;    


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
     
    # competition DATA
    competitionDate = "03.07.2020"
    #competitionDate = "16.08.2020"

    #competitionName = "UBS Kids Cup"
    competitionName = "Jahresmeisterschaft UBS Kids Cup"
    #competitionName = "Die schnällste Oberländer (Giele)"

    competitionLocation = "Interlaken"
    competition = Competition(competitionLocation, competitionDate, competitionName)

    #resultsFile = "tafExports/ubskidscupintern2020.csv" #source 57
    resultsFile = "tafExports/Jahresmeisterschaft_la_2020.csv" #source 58
    #resultsFile = "tafExports/ubskidscup2020.csv" #source 60
    #resultsFile = "tafExports/oberlandergiele2020.csv"  # source 61

    # SOURCE. for each competition please create a new source entry in the source db on phpmyadmin
    source = 58
     
    # FIND ATHLETES TO INSERT
    notExistingAthletes = findAthletesToInsert(resultsFile, urlCheckAthlete)
         
    for (name, yob, gender) in notExistingAthletes:
        if confirm("Insert %s, Yob: %s, %s To Database?" % (name, yob, gender)):
            athlete2tvustat.athlete2tvustat(urlathleteInsert, name, yob, gender, year+5)
            
    # UPLOAD
    notinsertedPerformances = uploadResults(url, competition, resultsFile, source, urlCheckAthlete)
    if len(notinsertedPerformances) > 0:
        exportPerformancesToCsv(notinsertedPerformances, "tafExports/notInsertedPerformances{}.csv".format(datetime.datetime.now().strftime("%Y%m%d%H%M")))
