'''
Created on 11.07.2020

@author: Lukas Sieber
'''
import xml.dom.minidom

from bs4 import BeautifulSoup
import requests
from _ast import If
from matplotlib.pyplot import table
from src.exportCSV import exportCSV
import json


def findpersonLIcenceNumber(contactId):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
#    
#     data = {"mobile": "false",
#             "blyear": year,
#             "acc": "ACC_1.BE.0159",
#             "blcat": blcat,
#             "disci": "DALL",
#             "top": "30"}
#     
#     mobile=false&blyear=2020&con=akb20-1ms3g5-esaosd8f-1-esc55wtt-3fl&top=30&srb=0
# #    
#     urlFrame = "https://www.swiss-athletics.ch/de/einzelner-athlet-bestenliste-neu/?"
# 
#     req = requests.post(urlFrame, data=data)
#     doc = BeautifulSoup(req.text, 'html.parser')
#     

    
def getText(node, tagname):
    child = node.getElementsByTagName(tagname)[0].firstChild
    if type(child).__name__!='NoneType':
        return child.data
    return None

def fromAlabustoTxt(alabusFile, txtFile):
    doc = xml.dom.minidom.parse(alabusFile)

    athletes = doc.getElementsByTagName("athlete")
    
    table = []
    
    for athlete in athletes:
        licenseSA = athlete.getAttribute("license")
        lastName = getText(athlete, "lastName")
        firstName = getText(athlete, "firstName")
        birthDate = getText(athlete, "birthDate")
        accountCode = getText(athlete, "accountCode")
        if type(accountCode) != None and type(birthDate) != None:
            clubID = accountCode 
            if clubID == "1.BE.0159":
                table.append([licenseSA, lastName, firstName, birthDate, clubID])
        else:
            print("******************************************************" + firstName + " " + lastName)

    exportCSV(table,txtFile);
    print("end")
    
def clearLicenses(rawFile, clearedFile):
    table = []
    with open(rawFile, mode="r", encoding="utf-8" ) as f:
        for line in f: 
            table.append(line.split(";"))
    
    unique_data = [list(x) for x in set(tuple(x) for x in table)]
    exportCSV(unique_data, clearedFile)
    return unique_data;

def updateAthleteLicense(firstName, lastName, birthDate,license, url):

    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    data = {"fullName": firstName + " " + lastName,
            "date": birthDate,
            "licenceNumber": license
            }
   
    req = requests.post(url, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    print(str(doc.text))
    j = json.loads(str(doc.text))
    return j["success"]

if __name__ == '__main__':
    rawExportFile = "allLicensesTVU.csv"
    #fromAlabustoTxt("../AlabusBase.xml", rawExportFile)
    clearedLicensesTVU = "clearedLicencesTVU.csv" 
    unique_data = clearLicenses(rawExportFile,clearedLicensesTVU)
  
    
    urlLocal = "http://localhost/statistik_tool_tvu/tvustat/public/updateAthleteLicence.php"
    urlWeb = "http://tvulive.bplaced.net/tvustat/public/updateAthleteLicence.php"

   
    changed = []
    notChanged = []
    
    i = 0
    for data in unique_data:
        
        if i> 10000:
            i = i+1
        else:
            print(data)
            i = i+1
            firstName = data[2]
            lastName = data[1]
            birthDate = data[3]
            licenseSA = data[0]            
            result = updateAthleteLicense(firstName, lastName, birthDate, licenseSA, urlLocal)
            change = [firstName, lastName, birthDate, licenseSA]
            if result:
                changed.append(change)
            else:
                notChanged.append(change)
             


    exportCSV(changed, "changedPeople.csv")
    exportCSV(notChanged, "NOTchangedPeople.csv")