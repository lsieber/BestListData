'''
Created on 27.02.2020

@author: Lukas Sieber
'''

class Athlete():
    '''
    classdocs
    '''


    def __init__(self, athleteId, athleteName, gender, birthDate, club):
        '''
        Constructor
        '''
        self.id = athleteId
        self.name = athleteName
        self.gender = gender
        self.club = club
        self.birthDate = birthDate
        self.birthYear = int(birthDate[-4:])
