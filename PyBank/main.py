import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

#Variables
total_months = 0
total_amount = 0
change_pl = []
change_mn = []


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    row_one = next(csvreader)
    previous_row = int(row_one[1])
    total_amount += int(row_one[1])
    total_months += 1


    for row in csvreader:

        # Total number of months 
        total_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        total_amount += int(row[1]) 

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average
        change = int(row[1]) - previous_row
        
        previous_row = int(row[1])
        change_pl += [change]
        change_mn += [row[0]]

    average = sum(change_pl)/len(change_pl)
    change_pl.insert(0,0)
    mon_change_dict = {change_mn[i]:change_pl[i] for i in range(len(change_mn))}

    max_value = max(mon_change_dict.values())
    max_key = [k for k, v in mon_change_dict.items() if v == max_value]

    min_value = min(mon_change_dict.values())
    min_key = [k for k, v in mon_change_dict.items() if v == min_value]

    # Print all calculations
    print("""
Financial Analysis
---------------------
    """)
    print(f'Total Months:{total_months}')
    print(f'Total: ${total_amount}')
    print(f'Average Change: ${round(average,2)}')
    #print(change_pl)
    # Print the greatest increase in PL
    print(f'Greatest Increase in Profits: {max_key[0]}(${max_value})')
    # Print the greatest decrease in PL
    print(f'Greatest Increase in Profits: {min_key[0]}(${min_value})')

with open('PyBank.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("---------------------------------------\n")
    text.write(f'Total Months:{total_months}\n')
    text.write(f'Total: ${total_amount}\n')
    text.write(f'Greatest Increase in Profits: {max_key[0]}(${max_value})\n')
    text.write(f'Greatest Increase in Profits: {min_key[0]}(${min_value})')