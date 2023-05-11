# 1. Importing the csv module to work with CSV files in VSC
import csv 

# 2. Using the open() function to open the election_data.csv file.
# This function returns a file object that can be used to read or write data to the file.
with open("/Users/emilioaristeguiflores/desktop/challenges/python-challenge/PyPoll/Resources/election_data.csv") as csvfile:

    # 3. Creating a csv.reader object using the csvfile object and specifying the delimiter used in the CSV file.
    # This object can be used to iterate over the rows of the CSV file and extract data.
    reader = csv.reader(csvfile, delimiter=",")

    # 4. Skip the header row 
    header = next(reader)

    # 5. Initialize variables
    total_votes = 0
    candidate_votes = {}
    candidates = []

    # 6. Loop through each row in the CSV file
    for row in reader:
        # 7. Increment the total vote count
        total_votes += 1

        # 8. Check if (if) candidate is already in list of candidates 
        # (Row[2]) refers to the value in the third column of the current row, which corresponds to the candidate name in this case.
        # If the candidate is not (not in), not in operator, already in the list, it adds the candidate to the list (candidates = []).
        # The append method (append) is used to add a candidate's name to the end of the list if the candidate is not already on the list.
        # When the code reads each row from the CSV file, it splits the row into individual fields, and the fields are stored as a list. 
        # Row[2] will contain the name of the candidate that the current row's voter voted for.
        if row[2] not in candidates:
            candidates.append(row[2])

        # 9. Add vote to candidate's vote count.
        # If (if) checks if row[2] contains the name of the candidate that the current row's voter voted for.
        # Using the in operator (in) to check (Candidate_votes), if candidate's name (stored in row[2]) is already a key in the candidate_votes dictionary  
        # If the candidate is in (candidates_votes), the candidate's vote count is incremented by 1 using candidate_votes[row[2]] += 1.
        # If the candidate is not in (candidates_votes), a new key-value pair is added to (candidates_votes) 
        # with the candidate's name as the key and a value of 1 
        # (this would signify the first vote for that candidate): candidate_votes[row[2]] = 1.
        if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
        else:
            candidate_votes[row[2]] = 1

# 10. Determine the winner of the election based on popular vote
# max() is a built-in Python function that returns the maximum value from a list or dictionary. 
# It returns the candidate name with the highest vote count.
# (candidate_votes) is a dictionary, contains the total number of votes each candidate received.
# (key) is a keyword argument that is passed to the max() function. 
# It specifies the function that should be used to determine the maximum value. 
# (candidate_votes.get) is used as the key function. 
# (get) is a method of dictionaries that returns the value associated with a given key. 
# By passing (candidate_votes.get) as the key function, 
# (max()) determines the maximum value based on the values in the (candidate_votes) dictionary.
# (winner) is a variable that stores the name of the winning candidate.
winner = max(candidate_votes, key=candidate_votes.get)

# 11. Print out the analysis in the desired format
# {} are used when printing variables
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

# 12. (for) will iterate for each candidate in (in) the (candidates) list
for candidate in candidates:

    # Calculates the (candidate) vote percentage by dividing their vote count (candidate_votes)
    # by the total number of votes cast in the election (total_votes) and multiplying by 100. 
    # (vote_percentage) variable stores the value
    vote_percentage = candidate_votes[candidate] / total_votes * 100

    # (print()) outputs a string with the (candidate) name
    # (vote percentage) (formatted to 3 decimal places using the :.3f format specifier)
    # total vote count using (candidate_votes[candidate])).
    print(f'{candidate}: {vote_percentage:.3f}% ({candidate_votes[candidate]})')

# 13. Print final results
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

14. # 19. Export to a txt file
# 
with open("PyPoll.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        vote_percentage = candidate_votes[candidate] / total_votes * 100
        txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes[candidate]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
