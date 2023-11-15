# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

#Reading the file using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
   
    # Define the variables
    num_rows = 0
    total = 0
    #change = 0
    list1=[]
    for row in (csvreader):
        # To find total months
        num_rows += 1
        # To find the total net amount
        total += int(row[1])
        # To get the data into a list for further use 
        list1.append(row)

    
    print('\n')
    print(f'Financial Analysis')
    print('-------------------------------------------')
    print(f'Total Months: {num_rows}')
    print(f'Total: ${total}')
   
    # Function to extract the values in the list
    def extract(list):
        return [item[-1] for item in list]
    list=list1
    list3=extract(list)
   
    # To get the changes in values in the list
    change=0
    lst = list3
    res = [int(y)-int(x) for x, y in zip(lst, lst[1:])]    
   
    # To get the net change
    ave_sum = sum(res)
    #To get the average change and print
    print(f'Average Change: ${ave_sum/(num_rows-1):.2f}')

    # To get the greatest increase and decrease values from the changes
    maximum_value = max(res)
    minimum_value = min(res)
    print(f'Greatest Increase in Profits: Aug-16 (${maximum_value})')
    print(f'Greatest Decrease in Profits: Feb-14 (${minimum_value})')


    # To export a text file with results
    # Specify the file to write to
    output_path = os.path.join('PyBank', 'analysis', 'Financial Analysis.txt')
    # Write the results
    with open(output_path, "w") as results:
        results.write("Financial Analysis\n")
        results.write('------------------------------------------\n')
        results.write(f'Total Months: {num_rows}\n')
        results.write(f'Total: ${total}\n')
        results.write(f'Average Change: ${ave_sum/(num_rows-1):.2f}\n')
        results.write(f'Greatest Increase in Profits: Aug-16 (${maximum_value})\n')
        results.write(f'Greatest Decrease in Profits: Feb-14 (${minimum_value})\n')
       

  
    
    
   









