import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("global_household_Financial_Dynamics.csv")

# Data Cleaning
df = df.drop_duplicates()

# New Column
df["Savings_Percentage"] = (df["Monthly_Savings"] / df["Total_Household_Income"] * 100)

# Average Income by Country
'''country_income = df.groupby("Country")["Total_Household_Income"].mean()
# Visualization
country_income.plot(kind="bar")
plt.title("Average Income by Country")
plt.xlabel("Country")
plt.ylabel("Income")
plt.show()'''
#Average Expense by Country
'''Country_expense=df.groupby('Country')["Monthly_Expenses"].mean()
Country_expense.plot(kind="bar")
plt.title("Average expenses by Country")
plt.xlabel("Country")
plt.ylabel("expense")
plt.show()'''
#Average savings by Country
'''Country_savings=df.groupby('Country')['Monthly_Savings'].mean()
Country_savings.plot(kind="bar")
plt.title("Average expenses by Country")
plt.xlabel("Country")
plt.ylabel("savings")
plt.show()'''

'''#Average Savings by City
city_savings = df.groupby("City")["Monthly_Savings"].mean()
print(city_savings)
#Top Performing Cities
top_performings=df.groupby("City")["Monthly_Savings"].mean().sort_values(ascending=False)
print()

#Fiancial Analysis
#Income vs Expenses Comparison
income_expenses = df.groupby("Country")[["Total_Household_Income","Monthly_Expenses"]].mean()
print(income_expenses)
#Tax Analysis
tax_analysis = df.groupby("Country")["Estimated_Taxes"].mean()
print(tax_analysis)
#Savings Distribution Analysis
savings_distribution = df.groupby("Country")["Monthly_Savings"].mean()
print(savings_distribution)
'''

#Automate Monthly Report Generation and Export to Excel
import pandas as pd

df = pd.read_csv("global_household_Financial_Dynamics.csv")

# Country Analysis
country_report = df.groupby("Country").agg({
    "Total_Household_Income": "mean",
    "Monthly_Expenses": "mean",
    "Monthly_Savings": "mean"})

# City Analysis
city_report = df.groupby("City")["Monthly_Savings"].mean().to_frame()

# Export to Excel
with pd.ExcelWriter("Financial_Report.xlsx", engine="openpyxl") as writer:
    country_report.to_excel(writer, sheet_name="Country Analysis")
    city_report.to_excel(writer, sheet_name="City Analysis")

print("Report exported successfully!")