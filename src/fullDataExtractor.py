from src.categoryIds import getCategoryIds
from src.findPersonIDs import findpersonIDs
from src.personParsing import getPersonBestList
from src.exportCSV import exportCSV


def extractTVUData(year, pathToData, categories, saveCategoryBestList):
    allAthleteIDs = {}
    for categoryName in categories:
        print("Starting With Category: " + categoryName.upper())
        categoryId = categories[categoryName]
        filename = pathToData + "data/{}/athleteIds/" + categoryName + "{}.csv"
        athleteIds = findpersonIDs(year, categoryId, categoryName, filename.format(year, year), saveCategoryBestList)
        
        # might be removed
        for x, y in athleteIds.items():
            allAthleteIDs[x] = y
         
        if not saveCategoryBestList:     
            for athleteName in athleteIds:
                print("Starting With Athlete: " + athleteName.upper())
                athleteId = athleteIds[athleteName]
                fileNamePerson = pathToData + "data/{}/resultsByAthlete/" + athleteName + "{}.csv"
                folder = year
                suffix = year
                if "TV Unterseen" in athleteName:
                    if athleteName[-2:-1] == "T":
                        suffix = "{}".format(year)[-2:]
                getPersonBestList(year, athleteId, fileNamePerson.format(folder, suffix))
                
    allathletes = []
    for k, v in allAthleteIDs.items():
        allathletes.append([k, v])
    exportCSV(allathletes, pathToData + "data/{}/allAthleteIds{}.csv".format(year, year))


if __name__ == "__main__":
    pathToData = "../../tvustat/"
    year = 2020
    
    allCategories = getCategoryIds()
    categories = {}
    ganzeGeschlecht = {}    
    for k,v in allCategories.items():
        if(k == "Alle Männer" or k == "Alle Frauen"):
            ganzeGeschlecht[k] = v
        else:
            categories[k] = v
            
    saveCategoryBestList = True
    extractTVUData(year, pathToData, ganzeGeschlecht, saveCategoryBestList)
    
    saveCategoryBestList = False
    extractTVUData(year, pathToData, categories, saveCategoryBestList)
