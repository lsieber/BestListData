# from src.upload.Performance import Performance
# from src.sa.config.disziplins import getDisziplinByTAF
# from src.upload.dataUploaderHelper import uploadPerformanceClass, \
#     checkAthleteExists
# from numpy.core.numeric import full
# from builtins import set
# from src.exportCSV import exportCSV
# import datetime
# 
# dictUBSKidsCup = {"60M": "60", "WEZ": "Weit Z", "BAL": "BALL200"}
# 
# 
# def uploadResults(url, competitionDate, competitionName, competitionLocation, resultsFile, source):
#     tvuID = "1.BE.0159"
#     
#     table = []
#     with open(resultsFile, mode="r") as f:
#         for line in f: 
#             table.append(line.split(";"))
#     
#     firstNameId = table[0].index("FirstName")
#     lastNameId = table[0].index("LastName")
#     birthYearId = table[0].index("Yob")
#     clubCodeId = table[0].index("ClubCode")
#     disziplinTafId = table[0].index("Event")
#     performanceId = table[0].index("Result")
#     windId = table[0].index("Wind")
#     
#     print(firstNameId)
#     
#     for l in table[1:20000]:
#         fullName = l[firstNameId] + " " + l[lastNameId] 
#         disziplin = getDisziplinByTAF(l[disziplinTafId])
#         detail = "" if disziplin.multiple == None else getDetailFromTable(disziplin.multiple, table, l[firstNameId], l[lastNameId], performanceId);
#         perf = l[performanceId].replace(".", "").replace(",", ".")
#         p = Performance(perf, fullName, l[birthYearId], competitionName, competitionLocation, competitionDate, disziplin.name, "", l[windId], detail, source)
#     
#         print("{} {} {} {} {}".format(p.name, p.disziplin, p.performance, p.competitionDate, p.wind))
#         uploadPerformanceClass(url, p)
# 
#         
# def getDetailFromTable(disziplins, table, firstName, lastName, pId):
#     detail = [];
#     for d in disziplins:
#         for l in table:
#             if firstName in l and lastName in l and d in l:
#                 detail.append(dictUBSKidsCup[d] + " " + l[pId].replace(".", "").replace(",", ".")) 
#     return "/".join(detail);
#     
#     
# def findAthletesToInsert(resultsFile, urlAthleteCheck):
#     tvuID = "1.BE.0159"
#     table = []
#     with open(resultsFile, mode="r") as f:
#         for line in f: 
#             table.append(line.split(";"))
#     
#     firstNameId = table[0].index("FirstName")
#     lastNameId = table[0].index("LastName")
#     birthYearId = table[0].index("Yob")
#     clubCodeId = table[0].index("ClubCode")
#     uniqueAthletes = set()
#     existingAthletes = set()
#     for l in table[1:10000]:
#         if l[clubCodeId] == tvuID:
#             fullName = l[firstNameId] + " " + l[lastNameId] 
#             birthYear = l[birthYearId]
#             if not (fullName, birthYear) in uniqueAthletes and not (fullName, birthYear) in existingAthletes :
#                 if not checkAthleteExists(urlAthleteCheck, fullName, birthYear):
#                     uniqueAthletes.add((fullName, birthYear))
#                 else:
#                     existingAthletes.add((fullName, birthYear))
#     exportCSV(uniqueAthletes, "notExistingAthletes{}.csv".format(datetime.datetime.now().strftime("%Y%m%d%H%M")))
#     if len(uniqueAthletes) == 0:
#         print("\n\nReady For Insertation. All Athletes are in the DB\n\n")
#         
#     
# if __name__ == '__main__':
#    
#     urlAthleteCheck = "http://tvulive.bplaced.net/tvustat/public/existing_entries.php"
#     urlLocalCheck = "http://localhost/statistik_tool_tvu/tvustat/public/existing_entries.php"
# 
#     urlLocal = "http://localhost/statistik_tool_tvu/tvustat/public/insertPerformanceWithCompetition.php"
#     urlWeb = "http://tvulive.bplaced.net/tvustat/public/insertPerformanceWithCompetition.php"
#     url = urlWeb
#     
#     # competition DATA
#     competitionDate = "2020-07-03"
#     competitionName = "UBS Kids Cup Intern"
#     competitionLocation = "Interlaken"
#     
#     resultsFile = "resultFiles/ubskidscupintern2020.csv"
#     # resultsFile = "resultFiles/ubskidscupintern2020.csv"
#     
#     # SOURCE. for each competition please create a new source entry in the source db on phpmyadmin
#     source = 57
#     
#     # FIND ATHLETES TO INSERT
#     findAthletesToInsert(resultsFile, urlAthleteCheck)
#         
#     # UPLOAD
#     # uploadResults(url, competitionDate, competitionName, competitionLocation, resultsFile, source)
#     
