'''
Created on 27.02.2020

@author: Lukas Sieber
'''

class Disziplin():
    '''
    This class represents a disziplin. it contains the disziplin Name, a Disziplin Id of the Swiss Athletics.
    '''


    def __init__(self, disziplinId, disziplinName, ascending, tafShortName = None, multipleTAF = None):
        '''
        Constructor
        '''
        self.id = disziplinId
        self.name = disziplinName
        self.ascending = ascending
        self.tafShortName = tafShortName
        self.multiple = multipleTAF