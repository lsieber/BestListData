'''
Created on 28.02.2020

@author: Lukas Sieber
'''
from src.blv.config import blvClubs

def performancefulfillsLimit(performance, limit):
    # TODO make this check more rigorous and cjeck other attributes such as the birth dat, the disziplin...
    if performance == None or limit == None:
        return False
    if performance.disziplin.id == limit.disziplin.id:
        if performance.athlete.birthYear == limit.birthYear and performance.athlete.gender == limit.category.gender:       
#             print("......................................................")
#             print("NEXT TEST for Diziplin: " + performance.disziplin.name)
#             print("Performance: " + str(performance.result) + " , Limit: " + str(limit.value))
#             test = performance.result <= limit.value if limit.disziplin.ascending else performance.result >= limit.value  
#             print( "Performance fullfils Limit: " + str(test))
            
            return performance.result <= limit.value if limit.disziplin.ascending else performance.result >= limit.value  
        return False
    return False

def clubIsBLV(club):
    return club.name in blvClubs.getClubNames() or club.id in blvClubs.getClubIds() #or "ACC_1.BE" in club.id

if __name__ == '__main__':
    pass

def time2sec(time_str):
    """Get Seconds from time."""
    splited = str(time_str).replace("m","").split(':')
    if len(splited) == 1:
        # w = Mehrkämpfe mit Wind
        return float(splited[0].replace("w", "").replace("*", "").replace("A",""))
    if len(splited) == 2:
        return int(splited[0]) * 60 + float(splited[1])
    if len(splited) == 3:
        return int(splited[0]) * 3600 + int(splited[1]) * 60 + float(splited[2])
    return None 

def sec2time(sec):
    """Get Seconds from time."""
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    if m == 0:
        return "%.2f" % s
    else:
        return "%i:%.2f" % (int(m), s)

def formatResult(result, disziplin):
    return sec2time(result) if disziplin.ascending else "%.2f" % result

def fromatResultOfPerformance(performance):
    return formatResult(performance.result, performance.disziplin)


            
