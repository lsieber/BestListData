from bs4 import BeautifulSoup
import requests
from src.categoryParsing import findbyIdentifiers
from src.blv.TalentSheet import TalentSheet
from src.blv.config.limits import limits
from src.blv.exportTalents import loadAllAthletes
from src.sa.config.disziplins import getDisziplinByid, getDisziplinByName,\
    getDisziplinIds
from src.elmt.Athlete import Athlete
from src.elmt.Club import Club
from src.elmt.Performance import Performance
from src.elmt.Competition import Competition
from src.blv.KaderSheet import KaderSheet
from networkx.algorithms.community.quality import performance

def getAllTalentResults(athlete, year):
    
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})  
    data = {"mobile": "false",
            "blyear": year,
            "con": athlete.id ,
            "blcat": athlete.gender,
            "disci": "DALL",
            "top": "30",
            "srb": "0"}
    urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlistathlete.xhtml?"
    
    req = requests.post(urlFrame, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')

    disz_tags = doc.find_all('h3')
    spans = doc.find_all('span')

    performances = []
    disziplin = None
    
    # ************************
    # If an Athlete has only one disziplin then we have to send a new request with the disziplin Id as a parameter
    # ************************
    if len(disz_tags) == 1: # or len(disz_tags) == 0:  # is one if an athlete has only one disziplin and zero for teams as they do not have an geburtsdatum
        for span in spans:
            if "Disziplin" in str(span):
                for select in span.find_all("select"):
                    for option in select.find_all("option"):
                        disciplinId = option.get("value")
                        if disciplinId in getDisziplinIds():
                            disziplin = getDisziplinByid(disciplinId)
                            if disziplin == None:
                                print(disciplinId)
                            data["disci"] = disciplinId
                            req = requests.post(urlFrame, data=data)
                            doc = BeautifulSoup(req.text, 'html.parser')

    # ************************
    # Evaluation of the results of one athlete
    # ************************
    output = ["Resultat", "Rang", "Wettkampf", "Ort", "Datum", "Name", "Wind"]
    columNumber = {}
    disziplinName = False 
    disziplinNumber = 1  # because the first is the geburtsdatum
    for row in doc.find_all('tr'):
        columns = row.find_all('td')

        # Find the right columns for each defined output value within the next disziplin
        if row.text.strip()[:2] == "Nr":
            columns = row.find_all('th')
            columnCounter = 0
            for header in columns:
                if header.text.strip() in output:
                    columNumber[columnCounter] = header.text.strip()
                columnCounter += 1
            disziplinName = disz_tags[disziplinNumber].text.strip() if len(disz_tags) > 1 else disziplin.name
            disziplin = getDisziplinByName(disziplinName)
            disziplinNumber = disziplinNumber + 1
            
        else:
            columnCounter = 0
            values = {}
            values["Disziplin"] = disziplinName

            for column in columns:
                if columnCounter in columNumber:
                    if "Tooltip" in str(column):
                        values[columNumber[columnCounter]] = findbyIdentifiers(str(column), ':resultValue">', '</span>')
                        values["Bemerkung"] = findbyIdentifiers(str(column), '<div class="ui-tooltip-text ui-shadow ui-corner-all">', '</div>')
                    else:   
                        if "Es sind keine Daten vorhanden" not in str(row.text.strip()): 
                            values[columNumber[columnCounter]] = column.text.strip().replace("*", "")
                columnCounter += 1
            if "Es sind keine Daten vorhanden" not in str(row.text.strip()): 
                competition = Competition(values["Ort"], values["Datum"], values["Wettkampf"])
                wind = values["Wind"] if "Wind" in values else ""
                performance = Performance(values["Resultat"].replace("A",""), athlete,competition, disziplin, values["Rang"], wind )
                performances.append(performance)

            
    return performances

def evaluateTalents(year, athletes):
    csv_file_m = "limiten_M.csv"
    csv_file_w = "limiten_W.csv"
    limiten = limits()
    limiten.load(csv_file_m, year)
    limiten.load(csv_file_w, year)

    sprintKader = KaderSheet("Sprint", limiten, ["150 m", "300 m"])
    hurdenKader = KaderSheet("Hürden", limiten)
    laufKader = KaderSheet("Lauf", limiten, ["500 m"])
    wurfKader = KaderSheet("Wurf", limiten)
    sprungKader = KaderSheet("Sprung", limiten)
    mehrkampfKader = KaderSheet("Mehrkampf", limiten)


    for athlete in athletes:
        talentSheet = TalentSheet(athlete, limiten)
        performances = getAllTalentResults(athlete, year)
        for performance in performances:
            talentSheet.addPerformance(performance)
            sprintKader.addPerformance(performance)
            hurdenKader.addPerformance(performance)
            laufKader.addPerformance(performance)
            wurfKader.addPerformance(performance)
            sprungKader.addPerformance(performance)
            mehrkampfKader.addPerformance(performance)

        fileNameAthlete = (str(year)+"/"+str(year)+performances[0].athlete.name+".csv").replace(" ", "")
        talentSheet.exportSheet(fileNameAthlete)

    sprintKader.exportSheet("sprint.csv")
    hurdenKader.exportSheet("hurden.csv")
    laufKader.exportSheet("lauf.csv")
    sprungKader.exportSheet("sprung.csv")
    wurfKader.exportSheet("wurf.csv")
    mehrkampfKader.exportSheet("mehrkampf.csv")

if __name__ == "__main__":
    athlete = Athlete("CONTACT.WEB.152121", "Xavier Fischer", "M", "08.10.2005",  Club("ACC_1.BE.0159", "TV Unterseen"))

    
#     results = getAllTalentResults(athlete, 2019)
    
#     csv_file_m = "limiten.csv"
#     limiten = limits()
#     limiten.load(csv_file_m, 2019)
#     talentSheet = TalentSheet(athlete, limiten)
#     for performance in results:
#         talentSheet.addPerformance(performance)
#     
#     talentSheet.exportSheet("xavi.csv")    
    
    athletes = loadAllAthletes("talentList.csv")
    evaluateTalents(2020, athletes)

    