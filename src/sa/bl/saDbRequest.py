

from bs4 import BeautifulSoup
import requests

URLBestList = "https://alabus.swiss-athletics.ch/satweb/faces/bestlist.xhtml?"
URLBestListClub = "https://alabus.swiss-athletics.ch/satweb/faces/bestlistclub.xhtml?"
URLBestListAthlete = "https://alabus.swiss-athletics.ch/satweb/faces/bestlistathlete.xhtml?"


def disziplinCategory(year, categoryId, disziplinId, top="500"):
    data = {"mobile": "false",
            "blyear": str(year),
            "blcat": categoryId,
            "disci": disziplinId,
            "top": "%s" % top}
    return sendRequest(data, URLBestList)


def club(year, blcat, clubId, top="30"):
    data = {"mobile": "false",
            "blyear": year,
            "acc": clubId,
            "blcat": blcat,
            "disci": "DALL",
            "top": "%s" % top}
    return sendRequest(data, URLBestListClub)


def athlete(athlete, year, top="30", disci="DALL"):
    data = {"mobile": "false",
            "blyear": year,
            "con": athlete.id ,
            "blcat": athlete.gender,
            "disci": "%s" % disci ,
            "top": "%s" % top,
            "srb": "0"}
    return sendRequest(data, URLBestListAthlete)


def sendRequest(data, url):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})  
    req = requests.post(url, data=data)
    return BeautifulSoup(req.text, 'html.parser')
