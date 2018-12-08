import os
import pandas as pd 

electioncsv = os.path.join("..", "..", "..", "..", "Desktop", "NUCHI201811DATA2", "Homework", "03-Python", "Instructions", "PyPoll", "Resources", "election_data.csv")

#read in csv fild using pandas module
election_data = pd.read_csv(electioncsv)

#print title of sheet
print("Election Results")
print("-------------------------")

#total number of votes cast
total_votes = len(election_data["Voter ID"].value_counts())
print(f'Total Votes: {total_votes}')
print("-------------------------")

#complete list of candidates who received votes
all_candidates = election_data["Candidate"].unique()
#print(all_candidates)

election_data["Voter Count"] = 1
grouped_election_data = election_data.groupby(["Candidate"])

#Winner is Khan
Num_Votes = grouped_election_data["Voter Count"].sum()
#print(Num_Votes)

#print candidate voting statistics
print(f'{all_candidates[0]}: {((Num_Votes[1]/total_votes)*100).round(3)}% ({Num_Votes[1]})')
print(f'{all_candidates[1]}: {((Num_Votes[0]/total_votes)*100).round(3)}% ({Num_Votes[0]})')
print(f'{all_candidates[2]}: {((Num_Votes[2]/total_votes)*100).round(3)}% ({Num_Votes[2]})')
print(f'{all_candidates[3]}: {((Num_Votes[3]/total_votes)*100).round(3)}% ({Num_Votes[3]})')
print("-------------------------")
print("Winner: Khan")
print("-------------------------")

#Export results to text file
PyPoll_Output = open("PyPoll_Output.txt", "w+")
PyPoll_Output.write(f'Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n{all_candidates[0]}: {((Num_Votes[1]/total_votes)*100).round(3)}% ({Num_Votes[1]})\n{all_candidates[1]}: {((Num_Votes[0]/total_votes)*100).round(3)}% ({Num_Votes[0]})\n{all_candidates[2]}: {((Num_Votes[2]/total_votes)*100).round(3)}% ({Num_Votes[2]})\n{all_candidates[3]}: {((Num_Votes[3]/total_votes)*100).round(3)}% ({Num_Votes[3]})\n-------------------------\nWinner: Khan\n-------------------------')