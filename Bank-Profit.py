#!/usr/bin/env python
# coding: utf-8

# In[61]:


# PyBank

#Dependencies
import csv
import os

#load the budget file
load_budget = os.path.join("budget_data.csv")
output_budget = os.path.join ("budget_analysis.txt")

# Look for financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["" ,0]
greatest_decrease = ["", 999999999999999999999]
total_net = 0

# Read the csv and convert it into dictionaries
with open(load_budget) as financial_data:
    reader = csv.reader(financial_data)
    
    #Read the header row
    header = next(reader)
    #print(header)

    
 #Extract first row to avoide appending to net-change_list
    first_row = next(reader)
    print(first_row)
    total_months = total_months + 1
    
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    #print(total_net)
    #print(prev_net)
    
    #loop throuhg your data
    for row in reader:
        #Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        print(total_net)
        
        #Track the net change
        net_change = int(row[1])-prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        #print(net_change_list)
        #print(month_of_change)
        
        if net_change > greatest_increase[1]:
             greatest_increase[0] = row[0]
             greatest_increase[1] =net_change
        #print(greatest_increase)
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[0] = net_change
            
    #Calculate the Average Net Change
    net_monthly_avg = sum(net_change_list)/len(net_change_list)
    
    output = (
        f"\nFinancial Analysis\n"
        f"======================\n"
        f"Total Months: {total_months}\n"
        f"Total : ${total_net}\n"
        f"Average Increase In Profits {greatest_increase [0]}, (${greatest_increase[1]})\n"
        f"Greatest Increase In Profits {greatest_decrease[0]}, (${greatest_decrease[1]})\n"
 )
print(output)

with open(file_to_output, "w") as text_file:
    txt_file-write(output)


# In[ ]:




