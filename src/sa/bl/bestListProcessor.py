from src.elmt.Performance import Performance
from src.elmt.Club import Club
from src.sa.staticUtils import findbyIdentifiers
from src.elmt.Athlete import Athlete
from src.elmt.AthleteMinimal import AthleteMinimal
from src.elmt.Competition import Competition

class bestListProcessor:
    '''
    classdocs
    '''
    BLNR_IDENTIFIER = "Nr"
    RESULT_IDENTIFIER = "Resultat"
    WIND_IDENTIFIER = "Wind"
    RANKING_IDENTIFIER = "Rang"
    ATHLETENAME_IDENTIFIER = "Name"
    CLUB_IDENTIFIER = "Verein"
    COMPETITION_IDENTIFIER = "Wettkampf"
    LOCATION_IDENTIFIER = "Ort"
    DATE_IDENTIFIER = "Datum"
    BIRTHDATE_IDENTIFIER = "Geb. Dat."

    def __init__(self):
        '''
        Constructor
        '''
        self.headers = None

    def updateHeaders(self, header_row):
        counter = 0
        self.headers = {}
        for header in header_row.find_all('th'):
            self.headers[header.text] = counter
            counter += 1
            
    def resultFromRow(self, row):
        element = self.getColumnElementOrNone(row, self.RESULT_IDENTIFIER)
        return findbyIdentifiers(str(element), 'resultValue">',"</span>")

    def resultDetailFromRow(self, row):
        if '<div class="ui-tooltip-text ui-shadow ui-corner-all">' in str(row):
            return findbyIdentifiers(str(row), '<div class="ui-tooltip-text ui-shadow ui-corner-all">', "</div>")
        #possibility to add more ways to get details e.g. team details
        return None
    def blNrFromRow(self, row):
        return self.getColumnElementTextOrNone(row, self.BLNR_IDENTIFIER)

    def windFromRow(self, row):
        return self.getColumnElementTextOrNone(row, self.WIND_IDENTIFIER)
     
    def rankingFromRow(self, row):
        return self.getColumnElementTextOrNone(row, self.RANKING_IDENTIFIER)
    
    def locationFromRow(self, row):
        return self.getColumnElementTextOrNone(row, self.LOCATION_IDENTIFIER)
    
    def dateFromRow(self, row):
        return self.getColumnElementTextOrNone(row, self.DATE_IDENTIFIER)
    
    def birthDateFromRow(self, row):
        return self.getColumnElementTextOrNone(row, self.BIRTHDATE_IDENTIFIER)
    
    def competitionNameFromRow(self, row):
        for column in row.find_all('td'):
            for link in column.find_all('a'):
                if "wettkampf-bestenliste-neu" in link.get("onclick"):
                    return link.text
        return None
    
    def clubFromRow(self, row):
        for column in row.find_all('td'):
            for link in column.find_all('a'):
                if "verein-bestenliste-neu" in link.get("onclick"):
                    return Club(findbyIdentifiers(link.get("onclick"), "acc=", "&blcat"), link.text)
        return None
    
    def athleteMinimalFromRow(self, row):
        for column in row.find_all('td'):
            for link in column.find_all('a'):
                if "einzelner-athlet-bestenliste-neu" in link.get("onclick"):
                    return AthleteMinimal(findbyIdentifiers(link.get("onclick"), "con=" , "&"), link.text.strip())
        return None
    
    def athleteFromRow(self, row, gender):
        aMin = self.athleteMinimalFromRow(row)
        birthDate = self.birthDateFromRow(row)
        birthDate = birthDate if len(birthDate) >= 4 else None
        return Athlete(aMin.id, aMin.name, gender, birthDate, self.clubFromRow(row))
    
    def competitionFromRow(self, row):
        return Competition(self.locationFromRow(row), self.dateFromRow(row), self.competitionNameFromRow(row))
    
    def performanceFromRow(self, row, gender, disziplin, athlete=None):
        athlete = self.athleteFromRow(row, gender) if athlete is None else athlete
        return Performance(self.resultFromRow(row), athlete, self.competitionFromRow(row), disziplin, self.rankingFromRow(row), self.windFromRow(row), self.resultDetailFromRow(row) )
    
    def getColumnElementOrNone(self, row, identifier):
        if identifier not in self.headers: 
            return None
        return row.find_all('td')[self.headers[identifier]]
    
    def getColumnElementTextOrNone(self, row, identifier):
        e = self.getColumnElementOrNone(row, identifier)
        return e.text if e is not None else None