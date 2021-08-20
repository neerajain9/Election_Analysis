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
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)    
    
    # print the header row..(next skips the 1st row)
    headers = next(file_reader)
    print(headers)   
    
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
# Method 1 (Preferred)
with open(file_to_save, 'w') as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the election")  
    txt_file.write("\n------------------------")  
    
    # txt_file.write("Arapahoe, ")    
    # txt_file.write("Denver, ")    
    # txt_file.write("Jefferson")    
    txt_file.write("\nArapahoe, \nDenver, \nJefferson")

###############################
# Method 2

# # Open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file. (write() function is from the os-module)
# outfile.write("Hello World!")

# # Close the file
# outfile.close()




