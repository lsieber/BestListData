from bs4 import BeautifulSoup
import requests
import json


def uploadPerformance(url, name, birthYear, cName, cDate, cLocation, disziplin, performance, wind, ranking, detail, source):

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
            "source": source
            }
   
    req = requests.post(url, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    print(doc.text)
    j = json.loads(str(doc.text))
    return j["success"]
    
def uploadPerformanceClass(url,p):
    return uploadPerformance(url, p.name, p.birthYear, p.competitionName, p.competitionDate, p.competitionLocation, p.disziplin, p.performance, p.wind, p.ranking, p.detail, p.source)      

def checkAthleteExists(url, name, birthYear):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    data = {"type": "athleteYearExists",
            "fullName": name,
            "year": birthYear
            }
   
    req = requests.post(url, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    print( name + doc.text)
    j = json.loads(str(doc.text))
    return j["success"]
