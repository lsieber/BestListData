import json

from bs4 import BeautifulSoup
import requests


def uploadPerformance(url, name, birthYear, cName, cDate, cLocation, disziplin, performance, wind, ranking, detail, source, saId = "NULL"):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    data = {"athleteName": name,
            "athleteYear": birthYear,
            "competitionName": cName,
            "competitionLocation": cLocation,
            "competitionDate": cDate,
            "disziplin": disziplin,
            "performance":performance,
            "wind": wind,
            "ranking": ranking,
            "detail": detail,
            "source": source,
            "athleteSaId" : saId
            }
   
    req = requests.post(url, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    print(doc.text)
    j = json.loads(str(doc.text))
    return j["success"]
    #return True

    
def uploadPerformanceClass(url, p, source):
    d = p.competition.date.split(".")
    date = "%s-%s-%s" % (d[2], d[1], d[0])
    return uploadPerformance(url, p.athlete.name, p.athlete.birthYear, p.competition.name, date, p.competition.location, p.disziplin.name, p.result, p.wind, p.rang, p.detail, source, p.athlete.id)      


def checkAthleteExists(url, name, birthYear):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    data = {"type": "athleteYearExists",
            "fullName": name,
            "year": birthYear
            }
   
    req = requests.post(url, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    j = json.loads(str(doc.text))
    return j["success"]
