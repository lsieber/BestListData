from bs4 import BeautifulSoup
import requests
from src.io.exportCSV import exportCSV
from src.io.categoryParsing import findbyIdentifiers



def getPersonBestList(year, personID, exportFile):
        # Set headers  
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    data = {"mobile": "false",
            "blyear": year,
            "con": personID ,
            "blcat": "W",
            "disci": "DALL",
            "top": "30",
            "srb": "0"}
   
    urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlistathlete.xhtml?"

    req = requests.post(urlFrame, data=data)
    doc = BeautifulSoup(req.text, 'html.parser')

    disz_tags = doc.find_all('h3')
    onlyDisziplin = "";
    spans = doc.find_all('span')

    if len(disz_tags) == 1 or len(disz_tags) == 0:  # is one if an athlete has only one disziplin and zero for teams as they do not have an geburtsdatum
        for span in spans:
#             print(str(span))
            if "Disziplin" in str(span):
                selects = span.find_all("select")
                for select in selects:
                    options = select.find_all("option")
                    for option in options:
                        disciplinId = option.get("value")
                        disName = option.text.strip()
                        onlyDisziplin = disName
                        data["disci"] = disciplinId
                        req = requests.post(urlFrame, data=data)
                        doc = BeautifulSoup(req.text, 'html.parser')

    ndis = 0  # starts at 0 
    row_tags = doc.find_all('tr')

    table = []
    if len(disz_tags) > 0:  # for teams
        birthYear = disz_tags[ndis].get_text()
        table.append(["Geb. Dat.", birthYear])
        ndis += 1  # because the first is the geburtsdatum

    for row in row_tags:
        columns = row.find_all('td')

        if row.text.strip()[:2] == "Nr":
            disziplinName = disz_tags[ndis].text.strip() if  len(disz_tags) >= 2 else onlyDisziplin 
            table.append([disziplinName, ""])
            ndis = ndis + 1
            columns = row.find_all('th')

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
                if "Es sind keine Daten vorhanden" not in str(row.text.strip()): 
                    table_row.append(column.text.strip().replace("*", ""))
        
        if row.text.strip()[:2] == "Nr":
            table_row.append("Tooltip");
        if tooltip != False:
            table_row.append(tooltip);
        else:
            table_row.append("");  
        table.append(table_row)
        
#         print(table[-1])
    
    exportCSV(table, exportFile)
    return table

        
if __name__ == "__main__":
    ids = {
    "Julian Zaugg20":    "4sgua-2an8zc-hsxoxs67-1-htpi98gj-52ej",
    "Timo Fahrenbruch20":    "CONTACT.WEB.147153",
    "Lukas Sieber20"  :  "akb20-1ms3g5-esaosd8f-1-esc55wtt-3fl",
    "TV Unterseen U14M20"  :  "akb20-7la2me-f2j0m1la-1-f2rxxv1h-63j",
    "TV Unterseen U12M20":    "akb20-bozb4p-eqvx5qug-1-ermf7ypl-7uk",
    "TV Unterseen U18M20" :   "a21aa-ogaf4d-jy7njhbg-1-jz9pl00n-45s1",
    
    "TV Unterseen U14W20":    "akb20-8tv3q-f1iu9o4w-1-f1msvmpk-3ur",
    "TV Unterseen U14WT2"  :  "akb20-7la2me-f2j0m1la-1-f2rxxvvf-63l",
    "TV Unterseen U16W20" :   "akb20-bozb4p-eqvx5qug-1-erx8a264-c51",
    "TV Unterseen U12W20":    "akb20-bozb4p-eqvx5qug-1-ermf7znv-7um",
    "TV Unterseen Frauen20":    "TEAM.WEB.101600"

    }
    
    var1 = "akb20-bozb4p-eqvx5qug-1-ermf7znv-7um"
    
#     for name, athleteid in ids.items():

    getPersonBestList("2014", "CONTACT.WEB.145396", "Noelle Mühlheim" + "2014.csv")
