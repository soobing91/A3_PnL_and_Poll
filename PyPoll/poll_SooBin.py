import os
import csv

csvpath = os.path.join('.', 'election_data.csv')
outputpath = os.path.join('poll_SooBin.txt')

total = 0

votedFor = []
candList = []
results = {}
cand = []
votes = []
percent = []

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

    # Calculating percentages
    for candidate, vote in results.items():
        cand.append(candidate)
        votes.append(vote)
    
    for vote in votes:
        percentage = round(vote / total * 100, 2)
        percent.append('{0:.3f}'.format(percentage))
    
    # Gathering data into one
    final = list(zip(cand, votes, percent))

    # Declaring winner
    winning = max(votes)
    
    for elect in final:
        if elect[1] == winning:
            winner = elect[0]

# Print in console
print("Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total}\n"
    "-------------------------\n")
for printing in final:
    print(f"{printing[0]}: {printing[2]}% ({printing[1]})\n")
print("-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n")

# Creating a text file
txtfile = open(outputpath, 'w', newline = '')
txtfile.write("Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total}\n"
    "-------------------------\n")
for printing in final:
    txtfile.write(f"{printing[0]}: {printing[2]}% ({printing[1]})\n")
txtfile.write("-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n")
txtfile.close()