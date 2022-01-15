# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of cnadidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election on popular vote

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the results to
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

    # Read and analyze data here

    # Read thee file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)
    
    # for row in file_reader:
    #     print(row)



# # Import the datetime class from the datetime module.
# import datetime as dt

# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()

# # Print the Present Time
# print("The time right now is ", now)

# set file/path to load
# file_to_load = 'Resources/election_results.csv'

# # Open the file for reading
# election_data = open(file_to_load, 'r')

# # To Do - Perform analysis

# # Close the file
# election_data.close()

# # Open the file and read the file WITH statement
# with open(file_to_load) as election_data:

#     # to do: perform analyis
#     print(election_data)

# import csv
# import os
# # Assign a variable for the file to load and the path
# file_to_load = os.path.join("Resources","election_results.csv")

# #open the election results and read the file.
# with open(file_to_load) as election_data:
#     #Print the file object
#     print(election_data)

# import csv
# Initialize the Operating System Module
# import os

# # create a filename variable to a direct or indirect path to the file
# file_to_save = os.path.join("analysis","election_analysis.txt")
# # Using hte open() function with "w" mode we will write data to the file
# outfile = open(file_to_save,"w")

# # write to the file
# outfile.write("Counties in the Election\n-------------------------------------\n")

# #Carriage Return
# outfile.write("\nArapahoe\nDenver\nJefferson")

# # Close the file
# outfile.close