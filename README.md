# Election Anlysis Challenge

## Overview of Analysis

We have been asked to tabulate election results for a Colorado congressional race to determine the winner of the popular vote.  We also analyzed county vote counts to determine which had the highest turnout. The results are displayed on the command line for immediate viewing, and they are written to a text file for reference and distribution.  Python is used to create the script.

## Election Audit

Using the data analysis, we can answer several questions about the results including identifying the winner:

- Total votes cast = **369,711**
- County vote tallies
   -  Jefferson County:  **8,855** votes cast - **10.5%** of total votes
   -  Denver County:   **306,055** votes cast - **82.8%** of total votes
   -  Arapahoe County:  **24,801** votes cast -  **6.7%** of total votes
- **Denver County** residents casted the largest number of votes
-  Candidate vote tallies
   - Charles Casper Stockham:  **85,213** votes - **23.0%** of the votes
   - Diana DeGette:           **272,892** votes - **73.8%** of the votes
   - Raymon Anthony Doane:     **11,606** votes -  **3.1%** of the votes
- **Diana DeGette** won with **272,892** votes which is **73.8%** of the total vote

Below are images of the results from the Terminal Output and the File Output:

**Terminal Output**

![Terminal Output](/Resources/Terminal_Results.png)

**Text File Output**

![File Output](/Resources/File_Results.png)

## Summary and Future Use of Audit Script
 
To complete this audit, we wrote a program to read through the provided comma delimited file (CSV) containing votes and summarized all the individual lines contained within using a Python script.  The code was written so that it would run for any number of candidates across any number of counties for a single election.  If the committee wanted to have a repeatable election tabulation method for all elections, we would suggest extending the functionality of the script to maximize reusability, cost savings, and consistency.  The script is flexible so that it can be used for any election where the results are available in a common CSV format but we would recommend making at least the following 3 modifications:
 1.  Add a column into the CSV file to list out the unique election name.
 2.  Add a heading into the command line results and the text file to list the race name.
 3.  When creating the output text file name, concatenate on the race name to the file name so distinct race files are not overwritten.

