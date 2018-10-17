# Import the dataset by reading the CSV file 
import os
import csv

# Store List of Values
nameList = []
countList = []
candidate_votes = {}
candidateList = {}

total_votes = 0

PyPoll_CSV_Path = os.path.join('Resources', 'election_data.csv')
with open(PyPoll_CSV_Path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)     

    for row in csvreader:
        # Calculate the Total Number of Votes
        # total_votes = sum(1 for row in csvreader)

        # Get the candidate name from each row
        candidate_name = row[2]

        # Add to the total vote count
        total_votes = total_votes + 1

    # Loop Through the Candidate List
    
    #Here is our check condition.  nameList is where we store all the unique names, so this 'not in' condition will find new names
        if candidate_name not in nameList:

            # If the name at the currect index is not already in our nameList, we will add it there.
            nameList.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print Election Results 
print('Election Results')
print('---------------------------------')
print('Total Votes: ' + str(total_votes))
print('---------------------------------')

# Find the Percentages of Votes and Election Winner
maxVotes = 0 
for key in candidate_votes:
    if candidate_votes[key] > maxVotes:
        Winner = [key]
        maxVotes = candidate_votes[key]
    print(f'{key}: {round((candidate_votes[key]/total_votes)*100,2)}% ({candidate_votes[key]})')    
print('The winner of the election is : ' + str(Winner))

# Write Results to a Text File
with open("Election_Results.txt", "w+") as text_file:
     print('---------------------------------', file=text_file)
     print('Election Results', file=text_file)
     print('---------------------------------', file=text_file)
     print('Total Votes: ' + str(total_votes), file=text_file)
     print('---------------------------------')
     print(f'{key}: {round((candidate_votes[key]/total_votes)*100,2)}% ({candidate_votes[key]})', file=text_file)    
     print('---------------------------------', file=text_file)
     print('The winner of the election is : ' + str(Winner), file=text_file)