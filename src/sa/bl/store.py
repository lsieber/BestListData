
import json
import os
from src.io.exportCSV import exportCSV
from src.elmt.Performance import Performance
from src.elmt.Athlete import Athlete
from src.elmt.Competition import Competition
from src.elmt.Disziplin import Disziplin
from src.sa.config.disziplins import getDisziplinByid

def storeJson(filename, data):
    with open(filename, 'w') as json_file: 
        json.dump(data, json_file, ensure_ascii=False, indent=4)  # ensure_ascii=False, indent=4
    print("Stored data to file: %s" % filename)

        
def readJson(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data
    
def updateListJSON(filename, newEntry):
    if os.path.isfile(filename):
        data = readJson(filename)
        if not newEntry in data:
            data.append(newEntry)
            storeJson(filename, data)
    else:
        storeJson(filename, [newEntry])
            
def updateJson(filename, add_data):
    if os.path.isfile(filename):
        data = readJson(filename)
        for k, v in add_data.items():
            data [k] = v
        storeJson(filename, data)
    else:
        storeJson(filename, add_data)

def updateSecondLevelJson(filename, add_data):
    if os.path.isfile(filename):
        data = readJson(filename)
        for k, v in add_data.items():
            for vk, vv in v.items():
                data [k][vk] = vv
        storeJson(filename, data)
    else:
        storeJson(filename, add_data)

def updateAtheleteClubAffiliations(filename, performances):   
    if not os.path.isfile(filename):
        storeJson(filename, {})
    data = readJson(filename)
    for p in performances.values():
        athleteId = p["athleteId"]
        clubId = p["clubId"]
        year = p["date"][-4:]
        if athleteId not in data:
            data[athleteId]= {}
        if clubId not in data[athleteId]:    
            data[athleteId][clubId] = {}
        data[athleteId][clubId][year] = year
    storeJson(filename, data)
    table = [["AthletId", "ClubId", "Year"]]
    for aId, v in data.items():
        for cId, vv in v.items():
            for year in vv:
                table.append([aId, cId, year])
    exportCSV(table, filename+".csv")

def athleteToDict(athlete):
    return {"id":athlete.id, "name": athlete.name, "birth": athlete.birthDate, "birthYear": athlete.birthYear, "gender": athlete.gender, "club": athlete.club.id}

def dictToAthlete(di):
    return Athlete(di["id"],di["name"],di["gender"],di["birth"],di["club"])

def clubToDict(club):
    return {"name": club.name}

def performanceToDict(perf):
    return {"disziplinId": perf.disziplin.id, "result": perf.result, "wind":perf.wind, "ranking":perf.rang, "athleteId": perf.athlete.id, "clubId": perf.athlete.club.id, "date":perf.competition.date, "location":perf.competition.location,"competitionName":perf.competition.name, "detail":perf.detail}

def dictToPerformance(di, athletes):
    athlete = athletes[di["athleteId"]]
    competition = Competition(di["location"], di["date"], di["competitionName"])
    disziplin = getDisziplinByid(di["disziplinId"])
    return Performance(di["result"], athlete, competition, disziplin, di["ranking"], di["wind"], di["detail"])

def uniqueIdPerf(perf):
    return "%s%s%s%s%s%s" % (perf.disziplin.id[-8:], perf.result, perf.wind, perf.rang, perf.competition.date, perf.athlete.id[-8:])
