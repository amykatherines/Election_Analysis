# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of cnadidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election on popular vote

# initialize the csv module for file read/writes
import csv

# initialize the os module for system folder navigation 
import os



# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the results to
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initilize the total vote counter
total_votes = 0

# 1. declare the LIST for the distinct candidate names
candidate_options = []

# 2. declare the DICTIONARY for candidate name and votes
candidate_votes = {}

# Initialize the variables used to determine the winner
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    # Read and analyze data here

    # Read thee file object with the reader function
    file_reader = csv.reader(election_data)

    #Read header row
    headers = next(file_reader)

    # Read through each row in the CSV file
    for row in file_reader:
        # increase the vote_counter
        total_votes += 1

        # Get the candidate name from the 3rd column
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # 1. Add the candidate name to the list
            candidate_options.append(candidate_name)

            # 2. Begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0

        # increment the value in the dictionary where the key is the candidate_name
        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:

    #Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes {total_votes:,}\n"
        f"-------------------------\n"
    )

    # prints to the terminal, use the "end" parameter to ensure 
    # nothing is printed on the last line when file is written to again  
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)


    # 1. Iterate through the candidate list - Assign the "key" to the candidate_name variable
    for candidate_name in candidate_votes:

        # 2. Retrieve vote count of candidate which is the "Value" in teh key value pair
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes
        vote_percentage = votes/total_votes *100


        # #  Print the results
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Store the results in a variable for printing and writing to file
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print candidate results to terminal
        print(candidate_results)

        # write candidate results to file
        txt_file.write(candidate_results)

        # 1. Determine if the vote count is greater than the previously saved candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true set the values
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name



    # Print the winner
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
   
    print(winning_candidate_summary)
    # save the summary to our output file
    txt_file.write(winning_candidate_summary)





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