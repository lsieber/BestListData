from nt import link

from bs4 import BeautifulSoup
import requests

from src.blv import exportTalents
from src.blv.Utils import performancefulfillsLimit, clubIsBLV, time2sec
from src.blv.config.limits import limits
from src.elmt.Athlete import Athlete
from src.elmt.Club import Club
from src.elmt.Performance import Performance
from src.elmt.Competition import Competition


def scoutAll(year, limiten):
    talents = []
    for limit  in limiten.limitsClasses:       
        print(limit.disziplin.name + " " + str(limit.birthYear) + " Limite: " + str(limit.value))
        if limit.performanceYear == year:
            disziplinCategoryTalents = scoutTalent(int(year), limit)       
            talents.extend(disziplinCategoryTalents)
            for athlete in disziplinCategoryTalents:
                print(athlete.name + " " + str(athlete.birthYear))
                
    seen = set()
    return [ath for ath in talents if ath.id not in seen and not seen.add(ath.id)]

def scoutTalent(year, limit):
    # Set headers      
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    
    data = {"mobile": "false",
            "blyear": str(year),
#             "acc": "ACC_1.BE.0159",
            "blcat": limit.category.id,
            "disci": limit.disziplin.id,
            "top": "500"}
    
    urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlist.xhtml?"
 
    req = requests.post(urlFrame, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    
    emptyCompetition = Competition("NoLocation", "01.01." + str(year), "NoName")
    
    first_row = True
    col_headers = {}
    athletes = []
    
    for row in doc.find_all('tr'):
        if first_row:
            counter = 0;
            for header in doc.find_all('th'):
                counter += 1
                col_headers[header.text] = counter
            first_row = False
            
        result = 0
        birthDate = " "
        vereinId = " "
        vereinName = " " 
        athleteName = " "
        athleteId = " "
        columnCounter = 0
        for column in row.find_all('td'):
            columnCounter += 1
            if columnCounter == col_headers["Resultat"]: # maybe we have a better solution like scaning for resultValue
                result_byIdentifier = findbyIdentifiers(str(column), 'resultValue">',"</span>")
                result = time2sec(result_byIdentifier.replace("*", "").replace("A", ""))
            if columnCounter == col_headers["Geb. Dat."]:
                birthDate = column.text
            if columnCounter == col_headers["Rang"]:
                rang = column.text
                
            for link in column.find_all('a'):
                onclick = link.get("onclick")
                if "einzelner-athlet-bestenliste-neu" in onclick:
                    athleteName = link.text.strip()
                    athleteId = findbyIdentifiers(onclick, "con=" , "&")
                    
                if "verein-bestenliste-neu" in onclick:
                    vereinId = findbyIdentifiers(onclick, "acc=", "&blcat")
                    vereinName = link.text
        
        if result != 0:
            club = Club(vereinId, vereinName)
            if clubIsBLV(club):
                athlete = Athlete(athleteId, athleteName, limit.category.gender, birthDate, club)
                if int(limit.birthYear) == athlete.birthYear:
                    performance = Performance(result, athlete, emptyCompetition, limit.disziplin, rang)        
                    if performancefulfillsLimit(performance, limit):
                        athletes.append(athlete)      
    return athletes

def findbyIdentifiers(string, startIdentifier, endIdentifier):
    start = string.find(startIdentifier)+len(startIdentifier)
    end = string.find(endIdentifier, start, -1)
    return string[start:end]

if __name__ == "__main__":
    
    year = 2020
    
#     disziplinId = "5c4o3k5m-d686mo-j986g2ie-1-j986gefj-3vd"
#     categoryId = "5c4o3k5m-d686mo-j986g2ie-1-j986g45s-bk"
#     limit = 9.9
#     upper = True
#     limitBirthYear = 2004
#     blvClubList = blvClubs.getClubIds()
#       
#     ids = scoutTalent(year, categoryId, disziplinId, limit, upper, limitBirthYear, blvClubList)
#     print(ids)
    
    limiten = limits()
    limiten.load("limiten_M.csv", year)
    limiten.load("limiten_W.csv", year)
    
    talents = scoutAll(year, limiten)
    exportTalents.exportTalents(talents, "talentList.csv");

