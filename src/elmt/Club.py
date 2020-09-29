'''
Created on 27.02.2020

@author: Lukas Sieber
'''
from builtins import isinstance

class Club():
    '''        
    classdocs
    '''


    def __init__(self, clubId, clubName):
        '''
        Constructor
        '''
        
        self.id = clubId
        self.name = clubName
    
    def equals(self, club):
        if isinstance(club, Club):
            return self.id == club.id and self.name == club.name
        return False