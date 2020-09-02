'''
Created on 27.02.2020

@author: Lukas Sieber
'''

class Competition():
    '''
    classdocs
    '''


    def __init__(self, location, date, competitoinName):
        '''
        Constructor
        '''
        self.location = location
        self.date = date
        self.year = int(date[-4:])
        self.name = competitoinName
        