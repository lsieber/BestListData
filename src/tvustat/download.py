'''
Created on 03.10.2020

@author: lukas
'''
import os

from bs4 import BeautifulSoup
import requests

categoryIds = {
    "U10M" : [8],
    "U10W" : [9],
    "U12M" : [7],
    "U12W" : [10],
    "U14M" : [6],
    "U14W" : [11],
    "U16M" : [5],
    "U16W" : [12],
    "U18M-Man" : [1,2,3,4],
    "U18W-Wom" : [13, 14, 15, 16],
    }

if __name__ == '__main__':
    year = 2020
    os.chdir('C:/Users/lukas/Documents/TVU/tvustat/sa2tvu/%s' % year)
    print("working in directory: " + os.getcwd())
        
    urlWebDownload = "http://tvulive.bplaced.net/tvustat/public/bestList.php"
    urlLocalDownload = "http://localhost/tvustat/public/bestList.php"
    urlDownload = urlLocalDownload
    
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    for catName, categoryId in categoryIds.items():
        data = {
            "yearsControl": "ysingle",
            "years[]" : [year],
            "categoryControl": "multiple",
            "categories[]": categoryId,
            "disziplins[]": [],
            "top": 100,
            "keepTeam": "ALL",
            "keepPerson": "ATHLETE",
            "manualTiming": "E",
            "outputs":  "txtAsString"  # string {html, json, txt} defines which outputs are made. if no value is set the the default is html.
        }
        
    
        
        #urlTxt = "http://localhost/tvustat/public/txtExport.php"
        req = requests.post(urlDownload, headers = headers, data=data)
        doc = BeautifulSoup(req.text, 'html.parser')
    
        filename = "bestenlisten/bestenliste%s%s.txt" % (catName, year)
        print("writing file: " + filename)
        f = open( filename, "w")
        f.write(doc.text)
        f.close()
    
    print("worked through all Categories.")
