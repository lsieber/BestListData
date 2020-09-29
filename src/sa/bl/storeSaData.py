from src.sa.bl.store import athleteToDict, updateListJSON, performanceToDict, \
    readJson, dictToPerformance, dictToAthlete


def storeAthletes(filename, athletes):
    for athlete in athletes:
        storeAthlete(filename, athlete)


def storeAthlete(filename, athlete):
    updateListJSON(filename, athleteToDict(athlete))

    
def loadAthletes(filename):
    data = readJson(filename)
    athletes = []
    for d in data:
        athletes.append(dictToAthlete(d))
    return athletes


def storePerformances(filename, performances):
    for performance in performances:
        storePerformance(filename, performance)


def storePerformance(filename, performance):
    updateListJSON(filename, performanceToDict(performance))


def loadPerformances(filename, athletes):
    data = readJson(filename)
    performances = []
    for d in data:
        performances.append(dictToPerformance(d, athletes))
    return performances
