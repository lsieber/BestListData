from bs4 import BeautifulSoup
import requests
from src.categoryParsing import findbyIdentifiers

from src.elmt.Club import Club
from src.sa.config.categoryIds import getCategoryByid
from src.sa.bl.bestListProcessor import bestListProcessor
from src.sa.config.disziplins import getDisziplinByid
from src.sa.bl.store import athleteToDict, clubToDict, \
    performanceToDict, uniqueIdPerf, updateJson, updateAtheleteClubAffiliations


def getPersonTransferHistory(year, personID):
        # Set headers  
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    data = {"mobile": "false",
            "blyear": year,
            "con": personID ,
            "blcat": "M",
            "disci": "DALL",
            "top": "30",
            "srb": "0"}
   
    urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlistathlete.xhtml?"

    req = requests.post(urlFrame, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')

    first_row = True
    col_headers = {}
    clubids = []
    clubs = []
    for row in doc.find_all('tr'):
        if first_row:
            print(row)
            counter = 0;
            for header in doc.find_all('th'):
                print(header.text)
                counter += 1
                col_headers[header.text] = counter
            first_row = False
            print("middle")
            for header in row.find_all('th'):
                print(header.text)
            print("end")
            
        # columnCounter = 0
        for column in row.find_all('td'):
            print(column)
#             columnCounter += 1
#             if columnCounter == col_headers["Resultat"]: # maybe we have a better solution like scaning for resultValue
#                 result_byIdentifier = findbyIdentifiers(str(column), 'resultValue">',"</span>")
#                 result = time2sec(result_byIdentifier.replace("*", "").replace("A", ""))
#             if columnCounter == col_headers["Geb. Dat."]:
#                 birthDate = column.text
#             if columnCounter == col_headers["Rang"]:
#                 rang = column.text
#                 
            for link in column.find_all('a'):
                onclick = link.get("onclick")
                if "verein-bestenliste-neu" in onclick:
                    club = Club(findbyIdentifiers(onclick, "acc=", "&blcat"), link.text)
                    if club.id not in clubids:
                        clubs.append(club)
                        clubids.append(club.id)
    return clubs
        
        
def storePerformances(year, disziplinId, categoryId):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    
    data = {"mobile": "false",
            "blyear": str(year),
            "blcat": categoryId,
            "disci": disziplinId,
            "top": "500"}
    
    urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlist.xhtml?"
 
    req = requests.post(urlFrame, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    
    category = getCategoryByid(categoryId)
    gender = category.gender
    disziplin = getDisziplinByid(disziplinId)
    
    processor = bestListProcessor()
    performances = {}
    athletes = {}
    clubs = {}
    athleteClubs = {}
    firstRow = True
    for row in doc.find_all('tr'):
        if firstRow:
            processor.updateHeaders(row)
            firstRow = False
        else:
            p = processor.performanceFromRow(row, gender, disziplin)
            p.printDetails()
            performances[uniqueIdPerf(p)] = performanceToDict(p)
            athletes[p.athlete.id] = athleteToDict(p.athlete)
            clubs[p.athlete.club.id] = clubToDict(p.athlete.club)
            if p.athlete.id not in athleteClubs:
                athleteClubs[p.athlete.id] = {} 
            athleteClubs[p.athlete.id][p.athlete.club.id] = p.athlete.club.name
    updateJson("athletes.json", athletes)
    updateJson("clubs.json", clubs)
    updateJson("performances.json", performances)
    updateAtheleteClubAffiliations("athleteClubAffiliatons.json", performances)
    return performances        

    
if __name__ == "__main__":
    ids = {
    "Julian Zaugg20":    "4sgua-2an8zc-hsxoxs67-1-htpi98gj-52ej",
    "Timo Fahrenbruch20":    "CONTACT.WEB.147153",
    "TV Unterseen U14M20"  :  "akb20-7la2me-f2j0m1la-1-f2rxxv1h-63j",
    "TV Unterseen U12M20":    "akb20-bozb4p-eqvx5qug-1-ermf7ypl-7uk",
    "TV Unterseen U18M20" :   "a21aa-ogaf4d-jy7njhbg-1-jz9pl00n-45s1",
    
    "TV Unterseen U14W20":    "akb20-8tv3q-f1iu9o4w-1-f1msvmpk-3ur",
    "TV Unterseen U14WT2"  :  "akb20-7la2me-f2j0m1la-1-f2rxxvvf-63l",
    "TV Unterseen U16W20" :   "akb20-bozb4p-eqvx5qug-1-erx8a264-c51",
    "TV Unterseen U12W20":    "akb20-bozb4p-eqvx5qug-1-ermf7znv-7um",
    "TV Unterseen Frauen20":    "TEAM.WEB.101600"

    }
    
#     for year in range(2019, 2020):
#         clubs = getPersonTransferHistory(year, "akb20-1ms3g5-esaosd8f-1-esc55wtt-3fl")
#         print("Jahr %i:" % year)
#         for club in clubs: print(club.name)
    
    disziplinId = "5c4o3k5m-d686mo-j986g2ie-1-j986gfpc-4zv"
    categoryId = "5c4o3k5m-d686mo-j986g2ie-1-j986g45s-bk"
    categoryId = "W"
    
    for year in range(2005, 2021):
        storePerformances(year, disziplinId, categoryId)
    
