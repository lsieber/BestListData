'''
Created on 27.02.2020

@author: Lukas Sieber
'''
from src.blv.Utils import time2sec

class Limit():
    '''
    classdocs
    '''

    def __init__(self, limitValue, disziplin, category, birthYear, performanceYear, kader):
        '''
        Constructor
        '''
        self.value = time2sec(limitValue)
        self.disziplin = disziplin
        self.category = category
        self.birthYear = int(birthYear)
        self.performanceYear = performanceYear
        self.kader = kader