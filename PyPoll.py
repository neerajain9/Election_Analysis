# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:26:36 2021

@author: PNCSI
"""


# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete lis of candidates who received votes
# 3. The total number of votes each candidate received
# 4. percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# # Assign a variable for the file to load and the path.
# file_to_load = "Resources\election_results.csv"

# Assign a variable for the file to load and the path. (USING "OS" MODULE)
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file. (O/P File)
file_to_save = os.path.join("Analysis", "election_analysis.txt")

##############################
# Initialize the total vote counter
total_votes = 0

# Declare a list to capture the name of the candidates
candidate_options = []

# Declare a dictionary to capture the votes for the candidates
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)    
    
    # print the header row..(next skips the 1st row)
    headers = next(file_reader)


    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
 
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0           
        
        candidate_votes[candidate_name] += 1
 
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {votes} votes: {round((vote_percentage),1)}% of the total votes.")    
        # print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print(candidate_results)


        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    
    #Print the winner...
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    
    #print(f"{winning_candidate} won the campaign and received {winning_count} votes: {round((winning_percentage),1)}% of the total votes.")    
    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)

##############################
#Write the results to a text file
with open(file_to_save, 'w') as txt_file:
    txt_file.write("\nElection Results")  
    txt_file.write("\n------------------------\n")  
    
    txt_file.write(f'Total Votes: {votes:,}\n')    
    txt_file.write("------------------------\n")  
    for candidate_name in candidate_votes:
        txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    txt_file.write("------------------------\n")  
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write(f"Winning Vote Count: {winning_count:,}\n")
    txt_file.write(f"Winning Percentage: {winning_percentage:.1f}%\n")


    txt_file.write("------------------------\n")  

    # txt_file.write("Denver, ")    
    # txt_file.write("Jefferson")    
    #txt_file.write("\nArapahoe, \nDenver, \nJefferson")


    
#     # Print each row in the CSV file.
#     rowCount = 0
#     for row in file_reader:
#         rowCount = rowCount + 1
#         # Returns the list (type onject)...    
#         print(row) 
#         # print 1st element in the list... 
# #        print(row[0]) 
#     print(rowCount)
#     print(headers)
        
#    print(election_data)
    
#

##############################
# # Method 1 (Preferred)
# with open(file_to_save, 'w') as txt_file:
#     # Write some data to the file.
#     txt_file.write("Counties in the election")  
#     txt_file.write("\n------------------------")  
    
#     # txt_file.write("Arapahoe, ")    
#     # txt_file.write("Denver, ")    
#     # txt_file.write("Jefferson")    
#     txt_file.write("\nArapahoe, \nDenver, \nJefferson")

###############################
# Method 2

# # Open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file. (write() function is from the os-module)
# outfile.write("Hello World!")

# # Close the file
# outfile.close()




