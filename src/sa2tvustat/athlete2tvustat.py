import json
from bs4 import BeautifulSoup
import requests
import traceback

urlAthleteInsertationLocal = "http://localhost/tvustat/public/insertToDB.php"
urlAthleteInsertationWeb = "http://tvulive.bplaced.net/tvustat/public/insertToDB.php"

def athlete2tvustatClass(url, athlete, activeYear, licenseNumber = None, saId = None ):
    return athlete2tvustat(url, athlete.name, athlete.birthDate, athlete.gender, activeYear, licenseNumber, saId )
    
def athlete2tvustat(url, name, date, gender, activeYear, licenseNumber = None, saId = None ):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    genderId = 1 if gender == "M" or gender == "male" or gender =="m" else None
    genderId = 2 if genderId == None and (gender == "W" or gender == "female" or gender =="w") else genderId
    if genderId == None:
        print("Gender Id Could not be found. please check the definitions")
        print(traceback.format_exc())
    
    data = {"type": "athlete",
            "fullName": name,
            "date": date,
            "genderID": genderId,
            "teamTypeID" : 1, 
            "activeYear" : activeYear
            }
    if licenseNumber != None:
        data["licenceNumber"] = licenseNumber
    if saId != None:
        data["saID"] = saId    
        
    req = requests.post(url, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    j = json.loads(str(doc.text))
    return j["success"]

def confirm(confirmString):
    # raw_input returns the empty string for "enter"
    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}
    
    print(confirmString )
    print("y/n? (enter confirms with yes)")
    choice = input().lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print("confirm function has troubles")
        return False
    
if __name__ == '__main__':
    
    if confirm("thats something to confirm"):
        print("confirmed")
        
    #athlete2tvustat(urlAthleteInsertationLocal, "TESTLI2", "2012-02-04", "M", None, "2334-dfa2-23a-d")
    
    #athlete2tvustat(urlAthleteInsertationLocal, "TESTLI2", "2012-02-04", "M", None, "2334-dfa2-23a-d")