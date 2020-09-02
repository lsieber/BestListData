
from bs4 import BeautifulSoup
import requests
from src.blv.scoutTalents import findbyIdentifiers


def getAllDisziplins(year):
    # Set headers      
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    
#     data = {"mobile": "false",
#             "blyear": year,
# #             "acc": "ACC_1.BE.0159",
#             "blcat": limit.category.id,
#             "disci": limit.disziplin.id,
#             "top": "500"}
    data={"blyear": year}
    urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlist.xhtml?lang=de&mobile=false&initial=1"
 
    req = requests.post(urlFrame, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')
    
    for option in doc.find_all('option'):
        iddis = findbyIdentifiers(str(option), 'value="', '">')
        name = option.text
        
        print('Disziplin("' + iddis + '","' + name +'", True),')

def findbyIdentifiers(string, startIdentifier, endIdentifier):

    start = string.find(startIdentifier)+len(startIdentifier)
    end = string.find(endIdentifier, start, -1)
    return string[start:end]
    
if __name__ == "__main__":
    
    year = "2019"
 
    getAllDisziplins("2019")

