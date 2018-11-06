#Dependencies

import csv
import os

# Files to Load
csvpath = os.path.join("..", "C:/Users/beatl/Desktop/PyBank", "election_data.csv")

# Track the parameters

voter_id = []
Total_no_of_votes = 0
List_of_candidates_who_received_votes = []
voters = []
votes = []

# Read in the csv
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile)
     csv_header = next(csvfile)

# in this loop I did sum of column 1 which is revenue in csv file and counted total votes 
     for row in csvreader:
      List_of_candidates_who_received_votes.append(row[2])
      voter_id.append(row[0])
      

print("Election Results")
print("------------------------")
print("Total Votes:", len(voter_id))
print("------------------------")
