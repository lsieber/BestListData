'''
Created on 27.02.2020

@author: Lukas Sieber
'''
from src.blv.Utils import time2sec

class Performance:
    '''
    classdocs
    '''

    def __init__(self, result, athlete, competition, disziplin, rang, wind = None, detail = None):
        '''
        Constructor
        '''
        self.result = time2sec(result)
        self.athlete = athlete
        self.competition = competition
        self.disziplin = disziplin
        self.rang = rang
        self.wind = wind
        self.detail = detail


    def printDetails(self):
        print("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.disziplin.name,
            self.result,
            self.wind,
            self.rang,
            self.athlete.name,
            self.athlete.birthDate,
            self.competition.date,
            self.competition.location,
            self.competition.name,
            self.detail
            ))