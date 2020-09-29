# 
# import os
# from src.sa.bl import saDbRequest, getAllAthleteResults
# from src.sa.config.categoryIds import getCategories
# from src.sa.bl.bestListProcessor import bestListProcessor
# 
# def downloadResults(clubId, year):
#     athletes = findAllAthletesClub(clubId, year)
#     saveAthleteListJson(athletes)
#     saveAthleteListCsv(athletes)
#     performances = []
#     for athlete in athletes.values():
#         athPerfs = getAllAthleteResults.getAllAthleteResults(athlete, year)
#         performances.extend(athPerfs)
#         
#         
#         
# def findAllAthletesClub(clubId, year):
#     athletes = {}
#     for cat in getCategories():
#         doc = saDbRequest.club(year, cat.id, clubId, "500")
#         processor = bestListProcessor()
#         firstRow = True
#         for row in doc.find_all('tr'):
#             if firstRow:
#                 processor.updateHeaders(row)
#                 firstRow= False
#             else:
#                 athlete = processor.athleteFromRow(row, cat.gender)
#                 athletes[athlete.id] = athlete
#     return athletes
# 
# 
# if __name__ == '__main__':
#     year = 2020
#     os.chdir('C:/Users/lukas/Documents/TVU/tvustat/data/%s' %year)
#     print("working in directory: " + os.getcwd())
#   
#     