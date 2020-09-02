import csv

def exportCSV(table, filename):
    with open(filename, mode='w',  newline='', encoding='utf-8') as file:
        test_writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in table :
            #row.append(" ")
            test_writer.writerow(row)
    
    print("exported file" + filename)