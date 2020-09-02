import csv
from src.elmt.Club import Club
from src.elmt.Athlete import Athlete

def exportTalents(athletes, exportfile):

    with open(exportfile, 'w') as f:
        for a in athletes:
            f.write("%s;%s;%s;%s;%s;%s\n" % (a.id, a.name, a.gender, a.birthDate, a.club.id, a.club.name))
    
    print("exported file: " + exportfile)
        
def loadAllAthletes(file):
    athletes = []
    clubs = {}

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        for row in csv_reader:
            club = Club(row[4], row[5]) 
            if club.id not in clubs:
                clubs[club.id] = club
            else:
                club = clubs[club.id]
            athlete = Athlete(row[0],row[1],row[2],row[3],club)
            athletes.append(athlete)
    return athletes
        
            