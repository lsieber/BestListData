'''
Created on 27.02.2020

@author: Lukas Sieber
'''
from src.blv.Utils import time2sec

class Performance:
    '''
    classdocs
    '''

    def __init__(self, result, athlete, competition, disziplin, rang, wind = None):
        '''
        Constructor
        '''
        self.result = time2sec(result)
        self.athlete = athlete
        self.competition = competition
        self.disziplin = disziplin
        self.rang = rang
        self.wind = wind


