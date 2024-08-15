#import dependences 
import csv
import os 

#file path
file_path="Resources/budget_data.csv"
output_file="Analysis/budget_analysis.txt"

#initialize variables
total_months=0
net_amount=0
monthly_changes=[]
greatest_increase=["", 0]
greatest_decrease=["", float("inf")]

#read csv file
with open(file_path) as file:
    reader_csv=csv.reader(file)
    header=next(reader_csv)


#Get first row 
    first_row=next(reader_csv)
    previous_amount=int(first_row[1])
    total_months=total_months + 1
    net_amount=net_amount + int( first_row[1])

#Loop throughout the data
for row in reader_csv:

# Check if the row has the expected number of elements
    if len(row) < 2:
        print("Skipping row:", row)
        continue
        total_months=total_months + 1
        
        net_amount=net_amount + int( row[1])

#calculate profit and losses
        changes = int( row[1]) - previous_amount
        previous_amount = int( row[1])
        monthly_changes += [changes]

#find the greatest increase or decrease
        if changes > greatest_increase [1]:
         greatest_increase = [row[0], changes]

        if changes < greatest_decrease [1]:
         greatest_decrease = [row[0], changes]

#calculate average change
        average_change = sum(monthly_changes) / len(monthly_changes)


results = (
   
   f"Financial Analysis\n"
   f"-------------------\n"
   f"Total Months: {total_months}\n"
   f"Net Amount: {net_amount}\n"
   f"Average Change: ${average_change:.2f}\n"
   f"Greatest Increase: {greatest_increase}\n"
   f"Greatest Decrease: {greatest_decrease}\n"

   
)
         

print(results)

