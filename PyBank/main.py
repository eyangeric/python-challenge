import os
import pandas as pd 

budgetcsv = os.path.join("..", "..", "..", "..", "Desktop", "NUCHI201811DATA2", "Homework", "03-Python", "Instructions", "PyBank", "Resources", "budget_data.csv")

#read in csv fild using pandas module
budget_data = pd.read_csv(budgetcsv)

#Title of the Statistics 
print("Financial Analysis")
print("----------------------------")

#total number of months included in the dataset
total_months = len(budget_data["Date"].value_counts())
print(f'Total Months: {total_months}')

#total net amount of "profit/losses" over the entire period
net_amount = budget_data["Profit/Losses"].sum()
print(f'Total: ${net_amount}')

#average change in "profit/losses" between months over the entire period
#create list of monthly changes using a for loop
Monthly_Change_List = []
monthly_change  = 0
for i in range(1, len(budget_data["Profit/Losses"].value_counts())):
    monthly_change = budget_data.iloc[i, 1] - budget_data.iloc[i-1, 1]
    Monthly_Change_List.append(monthly_change)

# add value 0 to first index of list
Monthly_Change_List.insert(0, 0)

#create data column for monthly change
budget_data["Monthly_Change"] = pd.DataFrame({"Monthly_Change": Monthly_Change_List})

#average change rounded to 2 decimal places
average_change = budget_data["Monthly_Change"].sum()/len(range(1, len(budget_data["Profit/Losses"].value_counts())))
print(f'Average Change: ${average_change.round(2)}')

#greatest increase in profits over the entire period
max_increase = budget_data["Monthly_Change"].max()
month_of_max_increase = budget_data.iloc[budget_data[budget_data['Monthly_Change']==max_increase].index.item(), 0]
print(f'Greatest Increase in Profits: {month_of_max_increase} (${max_increase})')

#greatest decrease in profits over the entire period
max_decrease = budget_data["Monthly_Change"].min()
month_of_max_decrease = budget_data.iloc[budget_data[budget_data['Monthly_Change']==max_decrease].index.item(), 0]
print(f'Greatest Decrease in Profits: {month_of_max_decrease} (${max_decrease})')

#Export results to text file
PyBank_Output = open("PyBank_Output.txt", "w+")
PyBank_Output.write(f'Financial Analysis\n----------------------------\nTotal Months: {total_months}\nTotal: ${net_amount}\nAverage Change: ${average_change.round(2)}\nGreatest Increase in Profits: {month_of_max_increase} (${max_increase})\nGreatest Decrease in Profits: {month_of_max_decrease} (${max_decrease})')