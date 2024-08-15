#import dependences 
import csv
import os 

#file path
#file_path='budget_data.csv'

with open('C:/Users/enmwa/OneDrive/Desktop/python-challenge/PyBank/Resources/budget_data.csv', mode='r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
     
#initialize variables
total_months=0
net_amount=0
monthly_changes=[]
greatest_increase=["", 0]
greatest_decrease=["", float("inf")]
previous_amount=0

#read csv file


with open('C:/Users/enmwa/OneDrive/Desktop/python-challenge/PyBank/Resources/budget_data.csv', mode='r') as csvfile:
    csv_reader=csv.DictReader(csvfile)
    #csv_reader=csv.reader(csvfile)
    first_row=next(csv_reader)
    previous_amount=int(first_row['Profit/Losses'])
    total_months += 1
    net_amount += int(first_row['Profit/Losses'])
    #header=next(csv_reader)
    #print (first_row)

# #Get first row 
#   first_row=next(reader_csv)
#     previous_amount=int(first_row[1])
#     total_months+= 1
#     #net_amount+= int( first_row[1])

#Loop throughout the data
    for row in csv_reader:

# Check if the row has the expected number of elements
        if len(row) < 2:
         print("Skipping row:", row)

        total_months+= 1
        #net_amount+= int( row[1])
        net_amount += int(row['Profit/Losses'])

#calculate profit and losses

        changes = int( row['Profit/Losses']) - previous_amount
        previous_amount = int( row['Profit/Losses'])
        monthly_changes.append (changes)

#find the greatest increase or decrease

        if changes > greatest_increase [1]:
         greatest_increase = [row['Date'], changes]

        if changes < greatest_decrease [1]:
         greatest_decrease = [row['Date'], changes]

#calculate average change

#average_change= sum(monthly_changes) / len(monthly_changes)-1

average_change =sum(monthly_changes) / (total_months -1 )

results = (

   f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_amount}\n"  # Changed 'Net Amount' to 'Total' for consistency with expected outcome
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"  # Added formatting for currency
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"  # Added formatting for currency
)

   
#    f"Financial Analysis\n"
#    f"-------------------\n"
#    f"Total Months: {total_months}\n"
#    f"Net Amount: ${net_amount}\n"
#    f"Average Change: ${average_change:.2f}\n"
#    #f"Greatest Increase in profits: {greatest_increase[0]}\n"
#     f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n" 
#    #f"Greatest Increase in profits: {greatest_increase[1]}\n"
#    #f"Greatest Decrease in profits: {greatest_decrease[0]}\n"
#    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n" 
#    #f"Greatest Decrease in profits: {greatest_decrease[1]}\n"
   
# )
         
# 
# Write results to a text file
output_file="C:/Users/enmwa/OneDrive/Desktop/python-challenge/PyBank/Analysis.txt"
with open(output_file, 'w') as txt_file:
    txt_file.write(results)
    print (results)