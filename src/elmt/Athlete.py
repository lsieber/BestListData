'''
Created on 27.02.2020

@author: Lukas Sieber
'''
from src.elmt.AthleteMinimal import AthleteMinimal

class Athlete(AthleteMinimal):
    '''
    classdocs
    '''


    def __init__(self, athleteId, athleteName, gender, birthDate, club):
        '''
        Constructor
        '''
        super().__init__(athleteId, athleteName) 
        self.club = club
        self.gender = gender
        self.birthDate = birthDate
        self.birthYear = int(birthDate[-4:]) if birthDate is not None else None
    