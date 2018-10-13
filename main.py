# Import the dataset by reading the CSV file 
import os
import csv

# Store List of Values
months = []
revenue = []
rev_change = [] 

PyBank_CSV_Path = os.path.join('Resources', 'budget_data.csv')
with open(PyBank_CSV_Path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)     

    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

    # Total Number of Months
        total_months = set(months)

    # Total Net Amount of "Profit/Losses" (Revenue)
        net = sum(revenue)

    # Average Change in Profits/ Losses = 446309.04
        average = net/len(total_months)     

# In this loop I found average revenue change and max revenue change, and min revenue change. 
max_rev_change = 0
min_rev_change = 0

for i in range(1,len(revenue)):
    rev_change.append(revenue[i] - revenue[i-1])   
    max_rev_change = max(rev_change)
    min_rev_change = min(rev_change)
    max_rev_change_date = str(months[rev_change.index(max(rev_change))+ 1])
    min_rev_change_date = str(months[rev_change.index(min(rev_change)) + 1])
    
# Print Results 
print('---------------------------------')
print('Financial Analysis')
print('---------------------------------')
print('Total Months: ' +str(len(total_months)))
print('Total Net Revenue: $'+str(net))
print('Average Change in Revenue: $'+str(round(average, 2)))
print("Greatest Increase in Profits: "+str(max_rev_change_date))
print("Greatest Decrease in Profits : "+str(min_rev_change_date)) 

# Write Financial Analysis to Text File 
with open("Financial_Analysis.txt", "w+") as text_file:
    print('---------------------------------', file=text_file)
    print('Financial Analysis', file=text_file)
    print('---------------------------------', file=text_file)
    print('Total Months: ' +str(len(total_months)), file=text_file)
    print('Total Net Revenue: $'+str(net))
    print('Average Change in Revenue: $'+str(round(average, 2)), file=text_file)
    print(f"Greatest Increase in Profits: ${max_rev_change_date}", file=text_file)
    print(f"Greatest Decrease in Profits: ${min_rev_change_date}", file=text_file) 
 