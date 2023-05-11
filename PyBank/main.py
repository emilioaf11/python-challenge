# 1. Importing the csv module to work with CSV files in VSC
import csv 

# 2. Using the open() function to open the budget_data.csv file.
# This function returns a file object that can be used to read or write data to the file.
with open("/Users/emilioaristeguiflores/desktop/challenges/python-challenge/PyBank/Resources/budget_data.csv") as csvfile:

    # 3. Creating a csv.reader object using the csvfile object and specifying the delimiter used in the CSV file.
    # This object can be used to iterate over the rows of the CSV file and extract data.
    reader = csv.reader(csvfile, delimiter=",")

    # 4. Skip the header row 
    header = next(reader)
    
    # 5. Initialize variables
    total_months = 0
    total_profit = 0 
    previous_month_profit = 0
    dates = []
    profits_losses = []
    profit_changes = []
    # This function allows to iterate through the data
    first_row = next(reader)
    # Add 1 to total months because the next(reader) function is skipping the first value
    total_months += 1
    # Make the variable an integer and list the number [1] as the first row to read 
    previous_profit = int(first_row[1])

    # 6. Loop through the rows in the CSV file
    for row in reader:
        
        # 7. Count the total number of months
        total_months += 1
        
        # 8. Add the date and profit/loss to their respective lists
        # Append is allowing to count all the data
        dates.append(row[0])
        profits_losses.append(int(row[1]))

        # 9. Add the "Profit/Losses"
        # Count the rows # read the first row and then start the loop
        # It can be an if statement or other options to calculate # prev_profit and current_profit
        # The for loop continues and adds the total profit
        total_profit += int(row[1])
        
        # 10. The current profit is computed with the for loop 
        current_profit = int(row[1])
        # Compute the change for the average change of the data
        change = current_profit - previous_profit 
        # Reassign previous_profit 
        previous_profit = current_profit
        # We add all the values to the end of the data with append
        profit_changes.append(change)
        # Reassign previous_month_profit
        previous_month_profit = total_profit
        # Compute the final calculation of all the values
        average_change = sum(profit_changes) / len(profit_changes)
        # This function was used to check the results: print(f"check: {change} = {current_profit} - {previous_profit}")

    # 11. Calculate the greatest increase and decrease in profit/losses
    # To evaluate the code: using variables that only have one transformation at a time
    # By following three steps on this line, and printing them to return each value individually
    greatest_increase = max(profit_changes)
    greatest_increase_month = dates[int(profit_changes.index(greatest_increase))]
    greatest_decrease = min(profit_changes)
    greatest_decrease_month = dates[int(profit_changes.index(greatest_decrease))]

# 12. Print Financial Analysis
print("Financial Analysis")

# 13. Print a Separation
print("----------------------------")

# 14. Print Total Months
print("Total Months:", total_months)

# 15. Print Total
print("Total: $",total_profit)

# 16. Print Average Change #round func
print("Average Change: $",round(average_change,2))

# 17. Print Greatest Increase in Profits
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")

# 18. Print Greatest Decrease in Profits
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# 19. Export to a txt file
with open("./PyBank.txt", 'w') as txtfile:
    txtfile.write(f"""
    Financial Analysis
    ----------------------------
    Total Months:{total_months}
    Total: {total_profit}
    Average Change: $",round{average_change,2}
    Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
    Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
    """)