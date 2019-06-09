import os
import csv

csvpath = os.path.join('..', 'election_data.csv')

voterCount = 0

candList = []
candUnique = []

with open(csvpath, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    for row in csvreader:
        voterCount += 1
        candList.append(row[2])
        
for cand in candList:
        if cand not in candList:
            candUnique.append(cand)

print(candUnique)