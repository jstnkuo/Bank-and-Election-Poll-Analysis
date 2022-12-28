import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile)

    #move on to the next row to skip header
    next(csv_reader)

    #initialize variables
    candidates = []
    unique = []
    row_count = []
    vote_count = []
    row_count = 0
    candidate_votes = {}
    
    # Read through each row of data
    for row in csv_reader:

        #sum up the rows(total votes)
        row_count = row_count + 1

        #input the values of cadidates into list
        candidates.append(row[2])

    #each time the cadidate name appears, it means they got a vote
    for i in candidates:
        if i not in unique:
            unique.append(i)
            candidate_votes[i] = 0

        candidate_votes[i] = candidate_votes[i] + 1

    #add vote count of each candidate to list
    vote_count.append(candidate_votes.get("Charles Casper Stockham"))
    vote_count.append(candidate_votes.get("Diana DeGette"))
    vote_count.append(candidate_votes.get("Raymon Anthony Doane"))

    #function to return key from value
    def get_key(val):
        for key, value in candidate_votes.items():
            if val == value:
                return key
    winner = max(vote_count)

    #assign a variable to summary of result
    winning_candidate_summary = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: " + str(row_count) + "\n"
        f"-------------------------\n"
        f"1. " + str(unique[0]) + ": " + str(round(vote_count[0]/row_count*100, 3)) + "% (" + str(vote_count[0]) + ")\n"
        f"2. " + str(unique[1]) + ": " + str(round(vote_count[1]/row_count*100, 3)) + "% (" + str(vote_count[1]) + ")\n"
        f"3. " + str(unique[2]) + ": " + str(round(vote_count[2]/row_count*100, 3)) + "% (" + str(vote_count[2]) + ")\n"
        f"-------------------------\n"
        f"Winner: " + get_key(winner) + "\n"
        f"-------------------------"
        )

    print(winning_candidate_summary)

#export results to text file
with open('PyPoll_Results.txt', 'w') as f:
    f.write(winning_candidate_summary)
