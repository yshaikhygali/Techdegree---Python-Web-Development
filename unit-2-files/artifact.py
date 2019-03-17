import csv

with open('asian-20181028.csv',newline='') as csvfile:
    # artreader = csv.reader(csvfile, delimiter = '|')
    artreader = csv.DictReader(csvfile, delimiter = '|')
    rows = list(artreader)
    for row in rows[:3]:
        # print(', '.join(row))
        print(row['emuIRN'])
