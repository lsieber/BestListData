import os

from src.io.exportCSV import exportCSV
from src.sa.bl import saDbRequest
from src.sa.bl.bestListProcessor import bestListProcessor
from src.sa.config.categoryIds import getCategoryByid, getCategories,\
    getCategoryByName
from src.elmt.Club import Club


def findTVUAthletesCategory(year, blcat):
        # Set headers  
    doc = saDbRequest.club(year, blcat, "ACC_1.BE.0159")
    
    processor = bestListProcessor()
    category = getCategoryByid(blcat)
    
    athletes = {}
    for row in doc.find_all('tr'):
        ths = row.find_all('th')
        if len(ths) > 0:
            if ths[0].text == "Nr":
                processor.updateHeaders(row)
        else:
            if "Bitte Kategorie und Disziplin ausw" not in str(row):
                athlete = processor.athleteFromRow(row, category.gender)
                athlete.club = Club("ACC_1.BE.0159", "TV Unterseen")
                if "TV Unterseen" in athlete.name:
                    print("TEAMS occured: we have to solve that")
                    athlete.name = athlete.name + category.name
                athletes[athlete.id] = athlete
            else:
                print("Keine Resultate")
    return athletes.values()
#     row_tags = doc.find_all('tr')
# 
#     teamCounter = 0
#     ids = {}
#     for row in row_tags:
#         columns = row.find_all('td')
#         for column in columns:
#             links = column.find_all('a')  
#     
#             for link in links:
#                 onclick = link.get("onclick")
#                 if "einzelner-athlet-bestenliste-neu" in onclick:
#                     athlet = link.text.strip()
#                     idPositionStart = onclick.find("con=") + 4  # not including the con=
#                     idPositionEnd = onclick.find("&", idPositionStart, -1)
#                     athleteId = onclick[idPositionStart:idPositionEnd]
#                     if "TV Unterseen" in athlet:
#                         teamCounter += 1
#                         suffix = "";
#                         if teamCounter > 1:
#                             suffix = "T{}".format(teamCounter)
#                         athlet = "TV Unterseen " + catName + suffix
#                     ids[athlet] = athleteId
#        
#     table = [["athleteName", "swissAthleticsDBId"]]  
#     for name in ids:
#         table.append([name, ids[name]])
#         
#     exportCSV(table, exportfile)
#     return ids


def saveAthleteIdsCSV(athletes, filename):
    table = []
    for athlete in athletes:
        table.append([athlete.name, athlete.id, athlete.birthDate, athlete.gender])
    exportCSV(table, filename)


def findAllTVUAthletes(year):
    athletes = {}
    for cat in getCategories():
    #cat = getCategoryByName("U23W")
        print(cat.name)
        for athlete in findTVUAthletesCategory(year, cat.id):
            athletes[athlete.id] = athlete
    return athletes.values()
    
    
if __name__ == "__main__":
    
    year = 2020
    os.chdir('C:/Users/lukas/Documents/TVU/tvustat/sa2tvu/%s' % year)
    print("working in directory: " + os.getcwd())
    
    #athletes = findTVUAthletesCategory(year, "5c4o3k5m-d686mo-j986g2ie-1-j986g45w-bm")
    athletes = findAllTVUAthletes(year)
    saveAthleteIdsCSV(athletes, "athleteIDs.csv")
