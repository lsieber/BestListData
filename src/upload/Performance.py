'''
Created on 27.02.2020

@author: Lukas Sieber
'''
class Performance:
    '''
    classdocs
    '''

    def __init__(self, performance, name, birthYear, competitionName,competitionLocation, competitionDate, disziplin, ranking, wind, detail, source):
        '''
        Constructor
        '''
        self.performance = performance
        self.name = name
        self.birthYear = birthYear
        self.competitionName = competitionName
        self.competitionLocation = competitionLocation
        self.competitionDate = competitionDate
        self.disziplin = disziplin
        self.ranking = ranking
        self.wind = wind
        self.detail = detail
        self.source = source


