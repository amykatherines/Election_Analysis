# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""
# This script will read a CSV file for votes cast in an election.
# The format of the file is known and there is a header row
# The output from the processing will be written to the terminal
# And written to a file in the "analysis" folder.
# 2022.01.22 - AKS - Created this script

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options_list = []
candidate_votes_dict = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_dict = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# 2: Track the largest county and county voter turnout.
county_that_won_count = 0
county_that_won = ""

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]
        county = row[1]

        # 3: Extract the county name from each row.


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options_list:

            # Add the candidate name to the candidate list.
            candidate_options_list.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes_dict[candidate_name] = 0

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county not in county_list and county not in county_list:
            # vb: Append the new dictionary to the list
            county_list.append(county)

            # begin tracking the county votes
            county_dict[county] = 0
            
        # Add a vote to that candidate and county's counts
        candidate_votes_dict[candidate_name] += 1
        county_dict[county] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    # write to the text file
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_dict:

        # 6b: Retrieve the county vote count.
        votes = county_dict.get(county)
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100        

        # 6d: Print the county results to the terminal.
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})")

        # 6e: Print Results to terminal and Save the county votes to a text file.
        print(county_results)

        # add the carriage return to the file output string
        county_results = (f"{county_results}\n")

        txt_file.write (county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > county_that_won_count) :
            county_that_won_count = votes
            county_that_won = county


    # 7: Print the county with the largest turnout to the terminal.
    county_results = (f"\n-------------------------\n"
    f"Largest County Turnout: {county_that_won}\n"
    f"-------------------------\n")
        
    print(f"{county_results}")

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_results)
        
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes_dict:

        # Retrieve vote count and percentage
        votes = candidate_votes_dict.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
