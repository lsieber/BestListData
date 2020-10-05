import requests
from bs4 import BeautifulSoup
import json


if __name__ == '__main__':
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    #application/x-www-form-urlencoded
    print(headers)
    urlTxt = "http://localhost/tvustat/public/txtExport.php"
    data = "years%5B%5D=yall&yearsControl=yall&categories%5B%5D=13&categories%5B%5D=14&categories%5B%5D=15&categories%5B%5D=16&categoryControl=multiple&top=30&keepPerson=ATHLETE&keepTeam=YEARATHLETE&manualTiming=EORH&disziplins%5B%5D=all"
    
    data = {
        "yearsControl": "ysingle",
        "years[]" : [2020],
        "categoryControl": "multiple",
        "categories[]": [1,2,3,4],
        "disziplins": [],
        "top": 100,
        "keepTeam": "ALL",
        "keepPerson": "ATHLETE",
        "manualTiming": "E",
        "outputs":  "txt"  # string {html, json, txt} defines which outputs are made. if no value is set the the default is html.
    }
    print(data)
    
    req = requests.post(urlTxt, headers = headers, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    print(doc.text)
