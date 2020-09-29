'''
Created on 28.02.2020

@author: Lukas Sieber
'''
from src.sa.config.disziplins import getDisziplinByid, getDisziplinByName
import statistics
from src.blv.Utils import formatResult
from src.blv.Utils import fromatResultOfPerformance


class KaderSheet():
    '''
    classdocs
    '''

    def __init__(self, name, limits, additionalDisziplinNames=None):
        '''
        Constructor
        '''
        self.performancesByAthlete = {}
        self.otherLimitsByAthlete = {}
        self.otherPerformancesByAthlete = {}
        self.athletes = {}
        self.name = name
        self.limits = limits
        self.disziplins = []
        self.disziplinIds = []
        self.extractDisziplinsForKader(additionalDisziplinNames)
        
    def extractDisziplinsForKader(self, additionalDisziplinNames):
        for limit in self.limits.limitsClasses:
            if self.name == limit.kader:
                self.disziplins.append(limit.disziplin)
                self.disziplinIds.append(limit.disziplin.id)
                
        'Here We add additional relevant Disziplins to the Kadersheet which are not contained in the Limits. e.g. 150m in sprint'
        if additionalDisziplinNames != None:
            for disziplinName in additionalDisziplinNames:
                additionalDisziplin = getDisziplinByName(disziplinName)
                if additionalDisziplin == None:
                    print("could not find Disziplin " + disziplinName + " in our list. Maybe you have to add it to the disziplins list under src/sa/config")
                else:
                    if additionalDisziplin.id not in self.disziplinIds:
                        self.disziplins.append(additionalDisziplin)
                        self.disziplinIds.append(additionalDisziplin)
                        
    def addPerformance(self, performance):
        if performance.disziplin.id in self.disziplinIds:
            'ADDING THE ATHLETE if no result for him or her yet' 
            if performance.athlete.id not in self.performancesByAthlete:
                self.performancesByAthlete[performance.athlete.id] = {}
            'Adding the Disziplin if this athlete has no result in this disziplin yet'
            if performance.disziplin.id not in self.performancesByAthlete[performance.athlete.id]:
                self.performancesByAthlete[performance.athlete.id][performance.disziplin.id] = []
            'Adding the result'
            self.performancesByAthlete[performance.athlete.id][performance.disziplin.id].append(performance)
            
            'if the Result fulfills a limit we add this athlete to the list of this kader'
            if self.limits.performanceFulfillsOneLimit(performance):
                self.athletes[performance.athlete.id] = performance.athlete

        else:
            if self.limits.performanceFulfillsOneLimit(performance):
                if performance.athlete.id not in self.otherLimitsByAthlete:
                    self.otherLimitsByAthlete[performance.athlete.id] = {}
                if performance.disziplin.id not in self.otherLimitsByAthlete[performance.athlete.id]:
                    self.otherLimitsByAthlete[performance.athlete.id][performance.disziplin.id] = []
                self.otherLimitsByAthlete[performance.athlete.id][performance.disziplin.id].append(performance)
            else: 
                if performance.athlete.id not in self.otherPerformancesByAthlete:
                    self.otherPerformancesByAthlete[performance.athlete.id] = {}
                if performance.disziplin.id not in self.otherPerformancesByAthlete[performance.athlete.id]:
                    self.otherPerformancesByAthlete[performance.athlete.id][performance.disziplin.id] = []
                self.otherPerformancesByAthlete[performance.athlete.id][performance.disziplin.id].append(performance)
              
    def exportSheet(self, exportfile):
        with open(exportfile, 'w') as f:
            f.write("%s Kader\n" % self.name)
            f.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % ("Name", "Jg", "Geschl.", "Verein", "Disziplin", "SB", "Avg best 3", "Anzahl Resultate", "Limite", "Limite erreicht", "andere Limiten", "andere Leistungen"))

            for athleteId in self.athletes:
                firstRowAthlete = True
                athlete = self.athletes[athleteId]
                otherLimitString = self.getOtherLimitsStringOfAthlete(athlete.id)
                otherResultsString = self.getOtherResultsStringOfAthlete(athlete.id)
                
                for disziplinId in self.performancesByAthlete[athleteId]:
                    disziplin = getDisziplinByid(disziplinId)
                    performances = self.performancesByAthlete[athleteId][disziplinId]
                    
                    performances.sort(key=lambda p: float(p.result), reverse=not disziplin.ascending)
                    limit = self.limits.getLimitByPerformance(performances[0])
                    limitValue = "%s" % (formatResult(limit.value, disziplin)) if limit != None else "keine"
                    fullfillsLimit = "erfüllt" if self.limits.performanceFulfillsOneLimit(performances[0]) else ""
                    
                    bestResult = fromatResultOfPerformance(performances[0])
                    best3average = formatResult(statistics.mean(float(p.result) for p in performances[:3]), disziplin) if len(performances) >= 3 else ""
                    if firstRowAthlete:
                        f.write("%s;%s;%s;%s;%s;%s;%s;%i;%s;%s;%s;%s\n" % (athlete.name, athlete.birthYear, athlete.gender, athlete.club.name, disziplin.name, bestResult, best3average, len(performances), limitValue, fullfillsLimit, otherLimitString, otherResultsString))
                        firstRowAthlete = False
                    else:
                        f.write(";;;;%s;%s;%s;%i;%s;%s\n" % (disziplin.name, bestResult, best3average, len(performances), limitValue, fullfillsLimit))
                    
        print("exported file: " + exportfile)
    
    def getOtherLimitsStringOfAthlete(self, athleteId):
        otherLimits = []
        if athleteId in self.otherLimitsByAthlete:
            for disziplinId in self.otherLimitsByAthlete[athleteId]:
                performances = self.otherLimitsByAthlete[athleteId][disziplinId]
                performances.sort(key=lambda p: float(p.result), reverse=not getDisziplinByid(disziplinId).ascending)
                otherLimits.append(performances[0].disziplin.name + ": " + str(fromatResultOfPerformance(performances[0])))
        return  " / ".join(otherLimits)
    
    def getOtherResultsStringOfAthlete(self, athleteId):
        otherLimits = []
        if athleteId in self.otherPerformancesByAthlete:
            for disziplinId in self.otherPerformancesByAthlete[athleteId]:
                performances = self.otherPerformancesByAthlete[athleteId][disziplinId]
                performances.sort(key=lambda p: float(p.result), reverse=not getDisziplinByid(disziplinId).ascending)
                otherLimits.append(performances[0].disziplin.name + ": " + str(fromatResultOfPerformance(performances[0])))
        return  " / ".join(otherLimits)
    
     
