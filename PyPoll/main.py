# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Initilizing the variables to use in the loop
    total_votes = 0
    Charles_votes = 0
    Diana_votes = 0
    Raymon_votes = 0
    for row in (csvreader):
            # To get the total votes
        total_votes += 1
            # To get the votes for Charles Casper Stockham
        if row[2] =="Charles Casper Stockham":
            Charles_votes += 1
            # To get the votes for Diana DeGette
        elif row[2] =="Diana DeGette":
            Diana_votes += 1
            # To get the votes for Raymon Anthony Doane
        elif row[2] =="Raymon Anthony Doane":
            Raymon_votes += 1

    # Printing the results to the terminal
    print('\n')
    print('Election Results')
    print('------------------------------------------')
    print(f'Total Votes: {total_votes}')
    print('------------------------------------------')
    print(f'Charles Casper Stockham: {(Charles_votes/total_votes):.3%} ({Charles_votes})')
    print(f'Diana DeGette: {(Diana_votes/total_votes):.3%} ({Diana_votes})')
    print(f'Raymon Anthony Doane: {(Raymon_votes/total_votes):.3%} ({Raymon_votes})')
    print('------------------------------------------')
    
    # To map the candidates to their votes, creating dictionary
    candidate_votes_dict = {'Diana DeGette':Diana_votes,'Raymon Anthony Doane':Raymon_votes,'Charles Casper Stockham':Charles_votes}
    # Sorting the dictionary based on the values of the votes
    candidate_votes_dict=sorted((value, key) for (key,value) in candidate_votes_dict.items())
    sortdict=dict([(key,value) for value, key in candidate_votes_dict])
    # To retrieve the winner candidate with highest votes
    keys = [key for key in sortdict]
    print(f'Winner: {keys[-1]}')
    print('------------------------------------------')
    
    
    # To export a text file with results
    # Specify the file to write to
    output_path = os.path.join('analysis', "Election_Results.txt")
    # Write the results
    with open(output_path, "w") as results:
        results.write("Election Results\n")
        results.write('------------------------------------------\n')
        results.write(f'Total Votes: {total_votes}\n')
        results.write('------------------------------------------\n')
        results.write(f'Charles Casper Stockham: {(Charles_votes/total_votes):.3%} ({Charles_votes})\n')
        results.write(f'Diana DeGette: {(Diana_votes/total_votes):.3%} ({Diana_votes})\n')
        results.write(f'Raymon Anthony Doane: {(Raymon_votes/total_votes):.3%} ({Raymon_votes})\n')
        results.write('------------------------------------------\n')
        results.write(f'Winner: {keys[-1]}\n')
        results.write('------------------------------------------\n')
   
  

    
    
    
    
    
    
    
    
    
    
    
    
    