'''
Created on 09.02.2020

@author: Lukas Sieber
'''

import csv
from src.elmt.Limit import Limit
from src.sa.config.disziplins import getDisziplinByName, getDisziplinByid
from src.sa.config.categoryIds import getCategoryByName
from src.blv.Utils import performancefulfillsLimit


class limits:
    def __init__(self):
        self.limitsClasses = []
        
    
    def load(self, file_limits, year):
        with open(file_limits, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            line_count = 0
            for row in csv_reader:
                line_count += 1      
                if line_count == 1:
                    categories = row[1:-1]
                else:
                    if line_count == 2:
                        birthyears = row[1:-1]
                    else:                        
                        columcounter = 0
                        disziplin = getDisziplinByName(row[0])
                        if disziplin == None:
                            print(row[0] + " could not be found in the diszipln names. change writing")
                        for limit in row[1:-1]:
                            category = getCategoryByName(categories[columcounter])
                            birthYear = birthyears[columcounter]
                            performanceYear = int(year) # TODO
                            kader = row[-1]
                            if limit != "":
                                self.limitsClasses.append(Limit(limit, disziplin, category, birthYear, performanceYear, kader))
                            columcounter +=1

    def performanceFulfillsOneLimit(self, performance):
        for l in self.limitsClasses:
            if performancefulfillsLimit(performance, l):
                return True
        return False
    
    def getLimit(self, disziplinId, birthYear, performanceYear, gender):
        for l in self.limitsClasses:
            if l.disziplin.id == disziplinId and l.birthYear == birthYear and l.performanceYear == performanceYear and l.category.gender == gender:
                return l
        return None
    
    def getLimitByPerformance(self, performance):
        return self.getLimit(performance.disziplin.id, performance.athlete.birthYear, performance.competition.year, performance.athlete.gender)

if __name__ == '__main__':
    
    csv_file_m = "../limiten_M.csv"
    csv_file_w = "../limiten_W.csv"

    limits = limits()
    limits.load(csv_file_m, 2019)
    limits.load(csv_file_w, 2019)
    
    for l in limits.limitsClasses:
        print(l.disziplin.name + ", " + l.category.name + ", " + str(l.value) + ", " + str(l.birthYear)+ ", " + str(l.kader))
        
        
        