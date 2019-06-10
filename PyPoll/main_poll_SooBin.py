import os
import csv

csvpath = os.path.join('..', 'election_data.csv')

total = 0

votedFor = []
candList = []
results = {}

maximum = 0

with open(csvpath, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    for row in csvreader:
        
        # Total votes
        total += 1

        # Storing candidates
        votedFor.append(row[2])

        # List of candidates
        candidate = row[2]
        if candidate not in candList:
            candList.append(candidate)

            # Setting up a counter for a candidate found
            results[candidate] = 0

        # Number of votes counted
        results[candidate] += 1

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total}")

    # Calculating percentages
    for cand in results:
        numerator = results.get(cand)
        percent = round(numerator / total, 2)
        print(f"{cand}: {percent} ({numerator})")

        if results > maximum:
            maximum = results
            winner = cand
            print(cand)

    print("-------------------------")