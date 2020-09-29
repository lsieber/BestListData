from src.sa.bl import saDbRequest
from src.sa.config.disziplins import getDisziplinIds, getDisziplinByid,\
    getDisziplinByName
from src.sa.bl.bestListProcessor import bestListProcessor
from src.elmt.Athlete import Athlete


def getAllAthletesPerfromances(athletes, year):
    performances = []
    for athlete in athletes:
        performances.extend(getAllAthleteResults(athlete, year))
    return performances 

def getAllAthleteResults(athlete, year):

    doc = saDbRequest.athlete(athlete, year, "30", "DALL")
    
    disz_tags = doc.find_all('h3')
    disziplin = None
    
    # ************************
    # If an Athlete has only one disziplin then we have to send a new request with the disziplin Id as a parameter
    # ************************
    if len(disz_tags) == 1:  # or len(disz_tags) == 0:  # is one if an athlete has only one disziplin and zero for teams as they do not have an geburtsdatum
        for span in doc.find_all('span'):
            if "Disziplin" in str(span):
                for select in span.find_all("select"):
                    for option in select.find_all("option"):
                        disciplinId = option.get("value")
                        if disciplinId in getDisziplinIds():
                            disziplin = getDisziplinByid(disciplinId)
                            if disziplin == None:
                                print(disciplinId)
                            doc = saDbRequest.athlete(athlete, year, "30", disciplinId)

    # ************************
    # Evaluation of the results of one athlete
    # ************************
    performances = []
    processor = bestListProcessor()

    disziplinName = False 
    disziplinNumber = 1  # because the first (0) is the geburtsdatum
    for row in doc.find_all('tr'):
        if row.text.strip()[:2] == "Nr":
            processor.updateHeaders(row)
            
            disziplinName = disz_tags[disziplinNumber].text.strip() if len(disz_tags) > 1 else disziplin.name
            disziplin = getDisziplinByName(disziplinName)
            disziplinNumber = disziplinNumber + 1
            
        else:
            if "Es sind keine Daten vorhanden" not in str(row):
                p = processor.performanceFromRow(row, athlete.gender, disziplin, athlete)
                performances.append(p)
            
    return performances

if __name__ == '__main__':
    athlete = Athlete("akb20-1ms3g5-esaosd8f-1-esc55wtt-3fl", "Lukas Sieber", "M", "21.04.1993", "TV Unterseen TEST ONLy")
    results =  getAllAthleteResults(athlete, 2010)
    for performance in results:
        performance.printDetails()
    
    