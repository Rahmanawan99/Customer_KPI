import pandas as pd

# Load the Excel file
file_path = 'FTDH User Data.xlsx'
df = pd.read_excel(file_path)

# Convert 'device_count' to numeric, handling errors
df['device_count'] = pd.to_numeric(df['device_count'], errors='coerce')

# Drop NaN values from 'device_count'
device_counts = df['device_count'].dropna()

# Total user count
total_users = 7307

# ----------------------- #
# Step 1: Count users in different device count categories and calculate percentages
# ----------------------- #
count_one_device = (device_counts == 1).sum()
count_two_devices = (device_counts > 2).sum()
count_more_than_three = (device_counts > 3).sum()
count_more_than_four = (device_counts > 4).sum()
count_more_than_ten = (device_counts > 10).sum()
count_more_than_fifty = (device_counts > 50).sum()
count_more_than_hundred = (device_counts > 100).sum()

# Calculate percentages
percentage_one_device = (count_one_device / total_users) * 100
percentage_two_devices = (count_two_devices / total_users) * 100
percentage_more_than_three = (count_more_than_three / total_users) * 100
percentage_more_than_four = (count_more_than_four / total_users) * 100
percentage_more_than_ten = (count_more_than_ten / total_users) * 100
percentage_more_than_fifty = (count_more_than_fifty / total_users) * 100
percentage_more_than_hundred = (count_more_than_hundred / total_users) * 100

# ----------------------- #
# Step 2: Print the results
# ----------------------- #
print("Detailed Statistics on Device Count:")
print(f"Number of users with 1 device: {count_one_device} ({percentage_one_device:.2f}%)")
print(f"Number of users with 2 devices: {count_two_devices} ({percentage_two_devices:.2f}%)")
print(f"Number of users with more than 3 devices: {count_more_than_three} ({percentage_more_than_three:.2f}%)")
print(f"Number of users with more than 4 devices: {count_more_than_four} ({percentage_more_than_four:.2f}%)")
print(f"Number of users with more than 10 devices: {count_more_than_ten} ({percentage_more_than_ten:.2f}%)")
print(f"Number of users with more than 50 devices: {count_more_than_fifty} ({percentage_more_than_fifty:.2f}%)")
print(f"Number of users with more than 100 devices: {count_more_than_hundred} ({percentage_more_than_hundred:.2f}%)")
