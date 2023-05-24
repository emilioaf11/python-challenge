# python-challenge

## PyBank

### In this PyBank Challenge, you have to create a Python script to analyze the financial records of your company. This script will process a financial dataset named budget_data.csv, which contains two columns: "Date" and "Profit/Losses". The script will calculate various financial metrics and provide the following information:

- Total number of months included in the dataset
- Net total amount of "Profit/Losses" over the entire period
- Changes in "Profit/Losses" over the entire period, and the average of those changes
- Greatest increase in profits (date and amount) over the entire period
- Greatest decrease in profits (date and amount) over the entire period

I created lists to count all the months, profit and previous profit.
The dictionaries served to hold all the dates, profits losses and profit changes
The for loop counted all the months and profit changes to add them into the lists

The analysis should align with the following results:

### Financial Analysis

Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

## PyPoll

### In this PyPoll Challenge, you are tasked with helping a small, rural town modernize its vote-counting process. The provided dataset, election_data.csv, contains three columns: "Voter ID", "County", and "Candidate". Your Python script will analyze the votes and calculate the following values:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

The list held the total votes
The dictionaries served to count the votes for each candidate and the candidate

The analysis should align with the following results:

### Election Results

Total Votes: 369,711
Charles Casper Stockham: 23.049% (85,213)
Diana DeGette: 73.812% (272,892)
Raymon Anthony Doane: 3.139% (11,606)
Winner: Diana DeGette

## Contents


## Getting Started

To run the Python script and perform the vote counting analysis:

1. Make sure you have Python installed on your system.
2. Download the election_data.csv and the budget_data.csv files and place them in the same directory as the Python script.
3. Open a terminal or command prompt and navigate to the directory where the script and the dataset are located.
4. Execute the Python script by running the command: `python script.py` (replace `script.py` with the actual name of your Python script).

The scripts will print both analysis results to the terminal and export text files named "election_results.txt" and "budget_data.txt" with the same information.

## Contributions

If you would like to contribute to this project, you can follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your modifications and enhancements.
4. Test your changes thoroughly.
5. Submit a pull request, explaining the purpose and benefits of your modifications.

Please ensure that your contributions align with the goals of the project and adhere to the coding standards and best practices.

## Note

Ensure that you have the necessary permissions to read the dataset file and write the analysis results file in the execution directory.

Feel free to modify the script or adapt it to fit your specific needs.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact me at emilioaristegui@outlook.com 

Thank you for your interest in this project! Enjoy!
