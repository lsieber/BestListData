import os

from src.blv.Utils import performancefulfillsLimit, clubIsBLV
from src.blv.config.limits import limits
from src.sa.bl import saDbRequest
from src.sa.bl.bestListProcessor import bestListProcessor
from src.blv import exportTalents


def scoutAll(year, limiten):
    talents = []
    for limit  in limiten.limitsClasses:       
        print(limit.disziplin.name + " " + str(limit.birthYear) + " Limite: " + str(limit.value))
        if limit.performanceYear == year:
            disziplinCategoryTalents = scoutTalent(int(year), limit)       
            talents.extend(disziplinCategoryTalents)
            for athlete in disziplinCategoryTalents:
                print(athlete.name + " " + str(athlete.birthYear))
                
    seen = set()
    return [ath for ath in talents if ath.id not in seen and not seen.add(ath.id)]

def scoutTalent(year, limit):
    # sending request to the swiss athletics server and receiving the best list for a category, year, disziplin tuple with a max of 500 results
    doc = saDbRequest.disziplinCategory(year, limit.category.id, limit.disziplin.id, 500)

    athletes = []
    processor = bestListProcessor()
    first_row = True
    for row in doc.find_all('tr'):
        if first_row:
            processor.updateHeaders(row)
            first_row = False
        else:
            club = processor.clubFromRow(row)
            if club is not None:
                if clubIsBLV(club):
                    athlete = processor.athleteFromRow(row, limit.category.gender)
                    if int(limit.birthYear) == athlete.birthYear:
                        performance = processor.performanceFromRow(row, limit.category.gender, limit.disziplin)        
                        if performancefulfillsLimit(performance, limit):
                            athletes.append(athlete)
    return athletes

if __name__ == "__main__":

    year = 2020
    os.chdir('C:/Users/lukas/Documents/TVU/tvustat/blv/data/%s' %year)
    print("working in directory: " + os.getcwd())
  
    limiten = limits()
    limiten.load("input/limiten_M.csv", year)
    limiten.load("input/limiten_W.csv", year)
    
    talents = scoutAll(year, limiten)
    exportTalents.exportTalents(talents, "output/talentList.csv");

