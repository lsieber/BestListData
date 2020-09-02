import os
from src.upload.Performance import Performance
from src.upload.dataUploaderHelper import uploadPerformanceClass
from datetime import datetime
import csv

def loadPersonBestListFromDataTable(tablePath):
    performances = []
    with open(tablePath, encoding="utf-8") as f:
        name = "TODO"
        birthYear = False
        disziplin = False
        ids = False
        for line in f: 
            vals = line.split(";")
            if not birthYear:
                birthYear = vals[1][-10:];
            else: 
                if len(vals) == 2:
                    disziplin = vals[0]
                else:
                    if vals[0] == "Nr":
                        ids = None
                        ids = {k: v for v, k in enumerate(vals)} #stores the index of the collums in the ids class, https://stackoverflow.com/questions/36459969/python-convert-list-to-dictionary-with-indexes
                    elif len(vals) < 2:
                        print("No results for disziplin " + disziplin)   
                    else:
                        #Nr;Resultat;Wind;Rang;Name;Verein;Wettkampf;Ort;Datum;Tooltip;; 
                        performance = formatTime(vals[ids["Resultat"]])
                        wind = vals[ids["Wind"]] if "Wind" in ids else None
                        ranking = vals[ids["Rang"]]
                        name = vals[ids["Name"]]
                        competitionName = vals[ids["Wettkampf"]]
                        competitionLocation = vals[ids["Ort"]]
                        competitionDate = formatDate(vals[ids["Datum"]])
                        detail = vals[ids["Tooltip"]]
                        performances.append(Performance(performance, name, birthYear, competitionName, competitionLocation, competitionDate, disziplin, ranking, wind, detail, 1))
                        
    return performances        
            
def formatTime(potentialTimeValue):
    parts= potentialTimeValue.split(":")
    if len(parts) == 1:
        return potentialTimeValue
    elif len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    elif len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    else:
        raise RuntimeError("A not definded performance situation has occured")
    
def formatDate(date):
    year = date[-4:]
    month = date[3:5]
    day = date[:2]
    return "{}-{}-{}".format(year, month, day)
    
if __name__ == '__main__':
    urlLocal = "http://localhost/statistik_tool_tvu/tvustat/public/insertPerformanceWithCompetition.php"
    urlWeb = "http://tvulive.bplaced.net/tvustat/public/insertPerformanceWithCompetition.php"
    url = urlWeb
        
    year = 2020
    path = "../../../tvustat/data/{}/resultsByAthlete/".format(year)

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))
    print(files)
    notSucessfullInserted = [] 
    for f in files[:]:
        print(f)
        performances = loadPersonBestListFromDataTable(f)
        for p in performances:
            print("{} {} {} {} {}".format(p.name, p.disziplin, p.performance, p.competitionDate, p.wind))
            sucess = uploadPerformanceClass(url, p)
            if not sucess:
                notSucessfullInserted.append(p)
    filename= "NotInserted{}.csv".format(datetime.now().strftime("%Y_%m_%d_%H%M%S"))
    with open(filename, mode='w',  newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for p in notSucessfullInserted :
            writer.writerow([p.name, p.disziplin, p.performance, p.competitionDate, p.competitionName, p.competitionLocation, p.wind])
    print("exported file" + filename)
    
#     name = "Lukas Sieber"
#     birthYear = 1993
#     cName = "UBS Kids Cup Intern"
#     cDate = "2020-07-03"
#     cLocation = "Interlaken3"
#     disziplin = "100 m"
#     performance = 10.96
#     wind = None
#     ranking = None
#     detail = None
#     
#     uploadPerformance(name, birthYear, cName, cDate, cLocation, disziplin, performance, wind, ranking, detail)
# 
#     uploadPerformance(name, birthYear, "TEST", cDate, cLocation, disziplin, performance, wind, ranking, detail)

    