#Prepare election results analysis

#import dependencies
import os
import csv

#assign variable to get input data from
file_to_load = os.path.join("resources", "election_results.csv")
#assign variable to create output text file
file_to_save = os.path.join("analysis", "election_results.txt")

#open election results and read the file
with open(file_to_load) as election_data:

    #to do: read and analyze the data here

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #print the header row to make sure we get rid of it
    headers = next(file_reader)
    print(headers)