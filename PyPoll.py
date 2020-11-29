# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:      

    # Write three counties to the file.
    txt_file.write("Counties in the Election\n---------------------------------\nArapahoe\nDenver\nJeffferson")

    # Close the file
    txt_file.close()

    # To do: perform analysis
    print(election_data)

# The data we need to retrieve
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved votes.
# 3. Total number of votes each candidate recieved.
# 4. Percentage of votes each candidate won.
# 5. The winner of the election based on popular vote. 

# Close the file. -> Put here for now
election_data.close()