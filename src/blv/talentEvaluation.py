from src.blv.TalentSheet import TalentSheet
from src.blv.config.limits import limits
from src.blv.exportTalents import loadAllAthletes
from src.blv.KaderSheet import KaderSheet
from networkx.algorithms.community.quality import performance
from src.sa.bl import getAllAthleteResults
import os


def evaluateTalents(year, athletes, limiten):
    
    sprintKader = KaderSheet("Sprint", limiten, ["150 m", "300 m"])
    hurdenKader = KaderSheet("Hürden", limiten)
    laufKader = KaderSheet("Lauf", limiten, ["500 m"])
    wurfKader = KaderSheet("Wurf", limiten)
    sprungKader = KaderSheet("Sprung", limiten)
    mehrkampfKader = KaderSheet("Mehrkampf", limiten)

    for athlete in athletes:
        print(athlete.name)
        talentSheet = TalentSheet(athlete, limiten)
        performances = getAllAthleteResults(athlete, year)
        for performance in performances:
            talentSheet.addPerformance(performance)
            sprintKader.addPerformance(performance)
            hurdenKader.addPerformance(performance)
            laufKader.addPerformance(performance)
            wurfKader.addPerformance(performance)
            sprungKader.addPerformance(performance)
            mehrkampfKader.addPerformance(performance)

        fileNameAthlete = ("output/athletenProfile/" + str(year) + performances[0].athlete.name + ".csv").replace(" ", "")
        talentSheet.exportSheet(fileNameAthlete)

    sprintKader.exportSheet("output/sprint.csv")
    hurdenKader.exportSheet("output/huerden.csv")
    laufKader.exportSheet("output/lauf.csv")
    sprungKader.exportSheet("output/sprung.csv")
    wurfKader.exportSheet("output/wurf.csv")
    mehrkampfKader.exportSheet("output/mehrkampf.csv")


if __name__ == "__main__":
    #athlete = Athlete("CONTACT.WEB.152121", "Xavier Fischer", "M", "08.10.2005", Club("ACC_1.BE.0159", "TV Unterseen"))
    
    year = 2020
    os.chdir('C:/Users/lukas/Documents/TVU/tvustat/blv/data/%s' % year)
    print("working in directory: " + os.getcwd())
    
    athletes = loadAllAthletes("output/talentList.csv")
    limiten = limits()
    limiten.load("input/limiten_M.csv", year)
    limiten.load("input/limiten_W.csv", year)
 
    evaluateTalents(year, athletes, limiten)

    
