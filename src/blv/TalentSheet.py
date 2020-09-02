'''
Created on 28.02.2020

@author: Lukas Sieber
'''
from src.sa.config.disziplins import getDisziplinByid

class TalentSheet():
    '''
    classdocs
    '''


    def __init__(self, athlete, limits):
        '''
        Constructor
        '''
        self.performancesByDisziplin = {}
        self.athlete = athlete
        self.limits = limits
        
    def addPerformance(self, performance):
        if self.athlete.id == performance.athlete.id:
            if performance.disziplin.id not in self.performancesByDisziplin:
                self.performancesByDisziplin[performance.disziplin.id] = []
            self.performancesByDisziplin[performance.disziplin.id].append(performance)
            
    def exportSheet(self, exportfile):
        with open(exportfile, 'w') as f:
            for disziplinId in self.performancesByDisziplin:
                disziplin = getDisziplinByid(disziplinId)
                f.write("%s\n" % disziplin.name)
                for p in self.performancesByDisziplin[disziplinId]:
                    fulfillsLimit = "Limite erfüllt" if self.limits.performanceFulfillsOneLimit(p) else " "
                    f.write("%s;%s;%s;%s;%s;%s;%s\n" % (p.result, p.rang, p.wind,  p.competition.date, p.competition.location, p.competition.name, fulfillsLimit))
    
        print("exported file: " + exportfile)
        