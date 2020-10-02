from src.io.exportCSV import exportCSV

def exportPerformancesToCsv(performaces, filename):
    ps = []
    for p in performaces:
        ps.append([p.result, p.wind, p.rang, p.disziplin.id, p.disziplin.name, p.athlete.id, p.athlete.name, p.athlete.club, p.athlete.club, p.competition.name, p.competition.location, p.competition.date])
    exportCSV(ps, filename)