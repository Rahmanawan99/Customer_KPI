import pandas as pd

# Load the Excel file
file_path = 'FTDH User Data.xlsx'
df = pd.read_excel(file_path)

# Convert 'avg_closing_balance' to numeric, handling errors
df['avg_closing_balance'] = pd.to_numeric(df['avg_closing_balance'], errors='coerce')

# Drop NaN values from 'avg_closing_balance'
balances = df['avg_closing_balance'].dropna()

# Total user count
total_users = 7307

# ----------------------- #
# Step 1: Calculate basic statistics
# ----------------------- #
average_balance = balances.mean()
min_balance = balances.min()
max_balance = balances.max()

# ----------------------- #
# Step 2: Count users in different balance categories and calculate percentages
# ----------------------- #
count_zero = (balances == 0).sum()
count_less_than_500 = (balances < 500).sum()  # Count balances less than 500
count_less_than_1000 = (balances < 1000).sum()
count_more_than_5000 = (balances > 5000).sum()
count_more_than_50000 = (balances > 50000).sum()
count_more_than_100000 = (balances > 100000).sum()
count_more_than_250000 = (balances > 250000).sum()

# Calculate percentages
percentage_zero = (count_zero / total_users) * 100
percentage_less_than_500 = (count_less_than_500 / total_users) * 100
percentage_less_than_1000 = (count_less_than_1000 / total_users) * 100
percentage_more_than_5000 = (count_more_than_5000 / total_users) * 100
percentage_more_than_50000 = (count_more_than_50000 / total_users) * 100
percentage_more_than_100000 = (count_more_than_100000 / total_users) * 100
percentage_more_than_250000 = (count_more_than_250000 / total_users) * 100

# ----------------------- #
# Step 3: Print the results
# ----------------------- #
print("Detailed Statistics on Average Closing Balance:")
print(f"Average Closing Balance: {average_balance:.2f}")
print(f"Minimum Closing Balance: {min_balance:.2f}")
print(f"Maximum Closing Balance: {max_balance:.2f}")
print(f"Number of users with a closing balance of 0: {count_zero} ({percentage_zero:.2f}%)")
print(f"Count of users with balance less than 500: {count_less_than_500} ({(count_less_than_500 / total_users) * 100:.2f}%)")
print(f"Number of users with a closing balance less than 1000: {count_less_than_1000} ({percentage_less_than_1000:.2f}%)")
print(f"Number of users with a closing balance more than 5000: {count_more_than_5000} ({percentage_more_than_5000:.2f}%)")
print(f"Number of users with a closing balance more than 50,000: {count_more_than_50000} ({percentage_more_than_50000:.2f}%)")
print(f"Number of users with a closing balance more than 100,000: {count_more_than_100000} ({percentage_more_than_100000:.2f}%)")
print(f"Number of users with a closing balance more than 250,000: {count_more_than_250000} ({percentage_more_than_250000:.2f}%)")
