import csv
import os 


# Read the data into a DataFrame
file_path="Resources/election_data.csv"
output_file="Analysis/election_analysis.txt"

# Calculate the total number of votes cast
total_votes = len(data)

# Get a complete list of candidates who received votes
candidates = data["Candidate"].unique()

# Initialize dictionaries to store the total votes and percentage of votes for each candidate
candidate_votes = {}
candidate_percentages = {}

# Calculate the total number of votes each candidate won
for candidate in candidates:
    candidate_data = data[data["Candidate"] == candidate]
    total_candidate_votes = len(candidate_data)
    candidate_votes[candidate] = total_candidate_votes
    candidate_percentages[candidate] = (total_candidate_votes / total_votes) * 100

# Find the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
