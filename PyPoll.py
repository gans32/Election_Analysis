#Prepare election results analysis

#import dependencies
import os
import csv

#assign variable to get input data from
file_to_load = os.path.join("resources", "election_results.csv")
#assign variable to create output text file
file_to_save = os.path.join("analysis", "election_results.txt")

#Initialize a total vote counter
total_votes = 0

#initialize list of candidate names
candidate_options = []

#initialize votes per candidate
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election results and read the file
with open(file_to_load) as election_data:

    #to do: read and analyze the data here

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #exclude header row
    headers = next(file_reader)
    
    #get vote count for csv file
    for row in file_reader:
        total_votes += 1

        #get candidate names
        candidate_name = row[2]

        #Add name to list if it hasn't been added to the list yet
        if candidate_name not in candidate_options:
         candidate_options.append(candidate_name)

         #begin tracking candidate's vote count
         candidate_votes[candidate_name] = 0

        #increment vote count every time candidate's name shows up
        candidate_votes[candidate_name] += 1

#get percentage of votes per candidate
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100

    #print percentage
    print(f"{candidate_name}: received {int(vote_percentage)}% of the vote.")

    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
         # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    
#to-do: print out winning candidate, vote count, and vote percentage
print(f"{winning_candidate} won the election with a total of {winning_count} votes, {int(winning_percentage)}% of the vote.")
