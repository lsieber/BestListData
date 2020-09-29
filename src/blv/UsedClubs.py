# -*- coding: iso-8859-1 -*-

'''
Created on 01.09.2020

@author: lukas
'''
from src.blv.config.blvClubs import getClubs
import csv
import os

def getClubsFromXML():
    import xml.etree.ElementTree as ET
    root = ET.parse('athletica.xml').getroot()
    for type_tag in root.findall('accounts/account'):
        name = type_tag.find("accountName").text
        code = type_tag.find("accountCode").text
        if code[0:4] == "1.BE":
            print("        Club('ACC_%s', '%s')," % (code, name))


def exportClubList():
    table = []
    for club in getClubs():
        table.append([club.name, club.id])
    filename = "input/clubList.csv"
   
    with open(filename, mode='w', newline='', encoding='latin-1') as file:
        test_writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in table :
            test_writer.writerow(row)
    
    print("exported file" + filename)
    

if __name__ == '__main__':
    print("Hello World")
    year = 2020
    os.chdir('C:/Users/lukas/Documents/TVU/tvustat/blv/data/%s' % year)
    print("working in directory: " + os.getcwd())
 
    exportClubList()
