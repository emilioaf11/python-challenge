# 1. Importing the csv module to work with CSV files in VSC
import csv 

# 2. Using the open() function to open the election_data.csv file.
# This function returns a file object that can be used to read or write data to the file.
with open("/Users/emilioaristeguiflores/python-challenge/PyPoll/Resources/election_data.csv") as csvfile:

    # 3. Creating a csv.reader object using the csvfile object and specifying the delimiter used in the CSV file.
    # This object can be used to iterate over the rows of the CSV file and extract data.
    reader = csv.reader(csvfile, delimiter=",")

    # 4. Don't read the header row 
    header = next(reader)

    # 5. Initialize variables
    total_votes = 0
    
    # This function allows to iterate through the data
    first_row = next(reader)
    # Add 1 to total votes because the next(reader) function is skipping the first value
    total_votes += 1

    # 6. Loop through the rows in the CSV file
    for row in reader:
        
        # 7. Count the total number of votes
        total_votes += 1

    print("Total Votes:", total_votes)