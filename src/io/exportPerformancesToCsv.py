
def exportPerformancesToCsv(performaces):
    ps = []
    for p in performaces:
        ps.append([p.result, p.wind, p.ranking, p.disziplin.id, p.disziplin.name, p.athlete.id, p.athlete.name, p.athlete.club.id, p.athlete.club.name, p.competition.name, p.competition.location, p.competition.date])
    exportPerformancesToCsv(ps)