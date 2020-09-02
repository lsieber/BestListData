'''
Created on 24.07.2020

@author: Lukas Sieber
'''
import csv
from xml.dom.minidom import parse, parseString

def exportCSV(table, filename):
    with open(filename, mode='w',  newline='', encoding='utf-8') as file:
        test_writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in table :
            #row.append(" ")
            test_writer.writerow(row)
    
    print("exported file" + filename)
    
def loadXMLUBSKidsCup(file):
    return True

if __name__ == '__main__':
    xmlFileKidsCupDownload = "BZI Interlaken - Athletica_18_07_2020.xml"
    selteqExport = "exportTest.csv"
    
    dom = parse(xmlFileKidsCupDownload) 
    athletes = dom.getElementsByTagName("athlete")
    athletesEmail = []
    i = 1
    for athlete in athletes:
        if athlete.getAttribute("announcement") == "1":
            firstname = athlete.getElementsByTagName("firstName")[0].firstChild.data
            lastname = athlete.getElementsByTagName("lastName")[0].firstChild.data
            birthDate = athlete.getElementsByTagName("birthDate")[0].firstChild.data
            email = athlete.getElementsByTagName("email")[0].firstChild.data

            print("nr {}: {} {}, {}, {}".format(i, firstname, lastname, birthDate, email))
            i=i+1
            athletesEmail.append([firstname, lastname, birthDate, email])
            
    export=[]
    with open(selteqExport, mode="r") as f:
        for line in f: 
            athlete = line.split(";")
            firstname = athlete[3]
            lastname = athlete[4]
            birthYear = athlete[5]
            check = 0
            for athEm in athletesEmail:
                if athEm[0] == firstname and athEm[1]==lastname and athEm[2][-4:]== birthYear:
                    athlete.append(athEm[3])
                    check = check+1;
            if check > 1:
                print("\n\n\n\n\n *************3 CAREFUL: one Athlete occurs multiple times in Meail List ********** \n\n\n\n\n\n")
            export.append(athlete)
    
    exportCSV(export, "exportWithEmail.csv")   
