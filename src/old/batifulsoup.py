from bs4 import BeautifulSoup
import requests


def my_function():
        # Set headers  
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
   
    data = {"mobile": "true",
            "blyear": "2019",
            "acc": "ACC_1.BE.0159",
            "blcat": "5c4o3k5m-d686mo-j986g2ie-1-j986g45k-bg",
            "disci": "DALL",
            "top": "30"}
   
    urlFrame = "https://alabus.swiss-athletics.ch/satweb/faces/bestlistclub.xhtml?lang=de&mobile=false&mobile=false&blyear=2019&acc=ACC_1.BE.0159&blcat=5c4o3k5m-d686mo-j986g2ie-1-j986g45k-bg&top=30"
#    url = "https://www.swiss-athletics.ch/de/verein-bestenliste-neu/?mobile=false&blyear=2019&acc=ACC_1.BE.0159&blcat=5c4o3k5m-d686mo-j986g2ie-1-j986g45k-bg&top=30"
#     url = "http://www.swiss-athletics.ch/satweb/faces/bestlistclub.xhtml"
#    req = requests.get(urlFrame, headers)

    req = requests.post(urlFrame,data=data)
    soup = BeautifulSoup(req.content, 'html.parser')
    print(soup.prettify())
#     
    doc = BeautifulSoup(req.text, 'html.parser')

# Grab all of the rows
    row_tags = doc.find_all('tr')
    disz_tags = doc.find_all('h3')

    for dis in disz_tags:
        print(dis.text.strip())

#    Let's print the first 5
    ndis = 0
    for row in row_tags:
        if row.text.strip() == "NrResultatRangNameNat.Geb. Dat.WettkampfOrtDatum":
            print(disz_tags[ndis].text.strip())
            ndis = ndis+1
            
        print(row.text.strip())

if __name__ == "__main__":
    my_function()
