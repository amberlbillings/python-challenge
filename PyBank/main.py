# Amber Billings
# Homework 3
# Data Analytics and Visualization Cohort 3

import pandas as pd

csv_path = "Resources/budget_data.csv"

df = pd.read_csv(csv_path)

total_months = df["Date"].nunique()

total = df["Profit/Losses"].sum()

for i in range(1, total_months):
    df.loc[i, 3] = df.iloc[i, 1] - df.iloc[i-1, 1]

renamed_df = df.rename(columns={3:"Change"})

average_change = renamed_df["Change"].mean()

greatest_increase = renamed_df.sort_values("Change", ascending=False)

greatest_decrease = renamed_df.sort_values("Change", ascending=True)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase.iloc[0, 0]} (${greatest_increase.iloc[0,2]})")
print(f"Greatest Decrease in Profits: {greatest_decrease.iloc[0, 0]} (${greatest_decrease.iloc[0,2]})")

output = open("financialAnalysis.txt","w+")

output.write("Financial Analysis \n")
output.write("---------------------------- \n")
output.write(f"Total Months: {total_months} \n")
output.write(f"Total: ${total} \n")
output.write(f"Average Change: ${round(average_change, 2)} \n")
output.write(f"Greatest Increase in Profits: {greatest_increase.iloc[0, 0]} (${greatest_increase.iloc[0,2]}) \n")
output.write(f"Greatest Decrease in Profits: {greatest_decrease.iloc[0, 0]} (${greatest_decrease.iloc[0,2]}) \n")

output.close()