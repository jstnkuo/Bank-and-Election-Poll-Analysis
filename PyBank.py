import os
import csv

budget_data_csv = os.path.join("Instructions", "PyBank", "Resources", "budget_data.csv")

with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile)

    #move on to the next row to skip header
    next(csv_reader)

    #initialize variables
    month = []
    profit = []
    change = []
    row_count = 0
    net_total = 0
    avg_total = 0

    # Read through each row of data
    for row in csv_reader:

        #sum up the rows(total months)
        row_count = row_count + 1

        #input the values of each column into respective lists
        month.append(row[0])
        profit.append(int(row[1]))

    #calculate total profit and average change
    net_total = sum(profit)
    avg_total = round((profit[(len(profit)-1)]-profit[0])/(len(profit)-1), 2)

    #loop through each index in profit to obtain the change in each month
    for i in range(len(profit)-1):
        change.append(profit[i+1]-profit[i])

    #calculate max and min and obtain indexes of each
    max = max(change)
    index_max = change.index(max)
    max_month = month[(index_max)+1]
    min = min(change)
    index_min = change.index(min)
    min_month = month[(index_min)+1]

    #assign a variable to summary of result
    financial_analysis = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: " + str(row_count) + "\n"
        f"Total: $" + str(net_total) + "\n"
        f"Average change: $" + str(avg_total) + "\n"
        f"Greatest Increase in Profits: " + str(max_month) + " (" + str(max) + ")\n"
        f"Greatest Decrease in Profits: " + str(min_month) + " (" + str(min) + ")"
        )

    print(financial_analysis)

#export results to text file
with open('PyBank_Results.txt', 'w') as f:
    f.write(financial_analysis)