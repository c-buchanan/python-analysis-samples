# Import the dataset by reading the CSV file 
import os
import csv

# Store List of Values
votes = []


PyPoll_CSV_Path = os.path.join('Resources', 'election_data.csv')
with open(PyPoll_CSV_Path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)     

    for row in csvreader:
        votes.append(row[0])
        total_votes = set(votes) 
        





# Print Election Results 
print('---------------------------------')
print('Election Analysis')
print('---------------------------------')
print('Total Votes: ' + str(len(total_votes)))

