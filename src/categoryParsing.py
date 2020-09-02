from bs4 import BeautifulSoup
import requests
from src.exportCSV import exportCSV 
from _ast import If, Is

def categoryParsing(blcat, exportfile):
        # Set headers  
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
   
    data = {"mobile": "false",
            "blyear": "2019",
            "acc": "ACC_1.BE.0159",
            "blcat": blcat,
            "disci": "DALL",
            "top": "30"}
   
    urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlistclub.xhtml?"
#     urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlistclub.xhtml?lang=de&mobile=false&mobile=false&blyear=2019&acc=ACC_1.BE.0159&blcat=5c4o3k5m-d686mo-j986g2ie-1-j986g45k-bg&top=30"

    req = requests.post(urlFrame,data=data)
      
    doc = BeautifulSoup(req.text, 'html.parser')
    parseCategoryFromDoc(doc, exportfile)

def parseCategoryFromDoc(doc, exportfile):
    row_tags = doc.find_all('tr')
    disz_tags = doc.find_all('h3')
    ndis = 0 #starts at 0 because there are no othe h3

    table = []

    for row in row_tags:
        columns = row.find_all('td')

        if row.text.strip()[:2] == "Nr":
#             print(disz_tags[ndis].text.strip())
            table.append([disz_tags[ndis].text.strip()])
            ndis = ndis+1
            columns = row.find_all('th')


#         print(row.text.strip())
        table_row = []
        tooltip = False;
        for column in columns:
            if "Tooltip" in str(column):
                valueIdentifier = ':resultValue">'
                value = findbyIdentifiers(str(column), valueIdentifier, '</span>')
                tooltipIdentifier = '<div class="ui-tooltip-text ui-shadow ui-corner-all">'
                tooltip = findbyIdentifiers(str(column), tooltipIdentifier, '</div>')
                table_row.append(value)
            else:   
                table_row.append(column.text.strip().replace("*", ""))
       
        if row.text.strip()[:2] == "Nr":
            table_row.append("Tooltip");
        if tooltip != False:
            table_row.append(tooltip);
        else:
            table_row.append("");    
        table.append(table_row)
        

        
    exportCSV(table, exportfile)

def findbyIdentifiers(string, startIdentifier, endIdentifier):
    start = string.find(startIdentifier)+len(startIdentifier)
    end = string.find(endIdentifier, start, -1)
    return string[start:end]
            
def headerContainsDetails(columns):
    for column in columns:
        if("details" in column.get_text()):
            return True
    return False


if __name__ == "__main__":
    categoryParsing("M", "catParsing.csv")
