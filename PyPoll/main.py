import csv
import os 
import random

#initialize variables
total_votes=0
candidates={}
#previous_candidate_votes=0
winner = ""
winner_votes = 0
candidate_percentages = {}

# Read the data into a DataFrame
file_path="C:/Users/enmwa/OneDrive/Desktop/python-challenge/PyPoll/Resources/election_data.csv"
output_file="C:/Users/enmwa/OneDrive/Desktop/python-challenge/PyPoll/Analysis"



#read csv file
with open(file_path, mode= 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    #header=next(reader_csv)

# Loop throughout the data
    for row in csv_reader:
        total_votes += 1
        candidate_name = row['Candidate']

        # If the candidate is not in the dictionary, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Print candidates dictionary
print(f"Candidates: {candidates}")
print(f"Total Votes: {total_votes}")

# Calculate the percentage of votes each candidate won
winner = ""
winner_votes = 0
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = {'votes': votes, 'percentage': percentage}
    # Determine the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

#total_votes = sum(candidates.values())
#total_votes = sum(candidate['votes'] for candidate in candidates.values())

print(f"Candidates with percentages: {candidates}")

# Print the analysis results

results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)


for candidate, data in candidates.items():
    results += f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n"

results += (
    
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

print(results)


# Write results to a text file

output_file = "C:/Users/enmwa/OneDrive/Desktop/python-challenge/PyPoll/Analysis/election_results.txt"
with open(output_file, 'w') as txt_file:
    txt_file.write(results)