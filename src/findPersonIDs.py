from nt import link

from bs4 import BeautifulSoup
import requests

from src.categoryParsing import parseCategoryFromDoc
from src.exportCSV import exportCSV 


def findpersonIDs(year, blcat, catName, exportfile, saveCategoryBestList):
        # Set headers  
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    data = {"mobile": "false",
            "blyear": year,
            "acc": "ACC_1.BE.0159",
            "blcat": blcat,
            "disci": "DALL",
            "top": "30"}
   
    urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlistclub.xhtml?"

    req = requests.post(urlFrame, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    
    if saveCategoryBestList:
        parseCategoryFromDoc(doc, exportfile[:-4]+"allResults.csv")
    
    row_tags = doc.find_all('tr')

    teamCounter = 0
    ids = {}
    for row in row_tags:
        columns = row.find_all('td')
        for column in columns:
            links = column.find_all('a')  
    
            for link in links:
                onclick = link.get("onclick")
                if "einzelner-athlet-bestenliste-neu" in onclick:
                    athlet = link.text.strip()
                    idPositionStart = onclick.find("con=") + 4  # not including the con=
                    idPositionEnd = onclick.find("&", idPositionStart, -1)
                    athleteId = onclick[idPositionStart:idPositionEnd]
                    if "TV Unterseen" in athlet:
                        teamCounter += 1
                        suffix = "";
                        if teamCounter > 1:
                            suffix = "T{}".format(teamCounter)
                        athlet = "TV Unterseen " + catName + suffix
                    ids[athlet] = athleteId
       
    table = [["athleteName", "swissAthleticsDBId"]]  
    for name in ids:
        table.append([name, ids[name]])
        
    exportCSV(table, exportfile)
    return ids


if __name__ == "__main__":
    findpersonIDs("2020", "5c4o3k5m-d686mo-j986g2ie-1-j986g45k-bg", "TEST", "findPerson.csv")
