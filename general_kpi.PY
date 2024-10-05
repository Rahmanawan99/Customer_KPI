import pandas as pd
import matplotlib.pyplot as plt


# Load the Excel file
file_path = 'FTDH User Data.xlsx'
df = pd.read_excel(file_path)

# Convert 'Days till FTDH' and 'avg_closing_balance' to numeric (forcing any invalid entries to NaN)
df['Days till FTDH'] = pd.to_numeric(df['Days till FTDH'], errors='coerce')
df['avg_closing_balance'] = pd.to_numeric(df['avg_closing_balance'], errors='coerce')

# Convert 'Onboarding' and 'Deactivation' to datetime format
df['Onboarding'] = pd.to_datetime(df['Onboarding'], errors='coerce')
df['Deactivation'] = pd.to_datetime(df['Deactivation'], errors='coerce')

Check if the conversions were successful
print(df[['Days till FTDH', 'avg_closing_balance', 'Onboarding', 'Deactivation']].head())

Now continue with your analysis
General statistics after conversion
summary = df.describe()
print("\nGeneral Summary:\n", summary)

KPIs and insights

# 1. Total users
total_users = df['user_id'].nunique()
print(f"\nTotal unique users: {total_users}")

# 2. Status reason distribution (to see common deactivation reasons)
status_reason_counts = df['Status reason'].value_counts()
print(f"\nStatus reason distribution:\n{status_reason_counts}")

# 3. Average time till FTDH (Fraud Trigger Detection Horizon)
avg_days_till_ftdh = df['Days till FTDH'].describe()
print(f"\nAverage days till FTDH: {avg_days_till_ftdh}")

# 4. Newly onboarded vs non-new users
# Count newly onboarded vs old users
newly_onboarded_count = df['Newly Onboarded'].value_counts().get('New', 0)
old_users_count = df['Newly Onboarded'].value_counts().get('Old', 0)

print(f"\nNewly onboarded users: {newly_onboarded_count}")
print(f"Old users: {old_users_count}")


# 5. Device count distribution (To check for multiple device usage)
device_count_stats = df['device_count'].describe()
print(f"\nDevice count stats:\n{device_count_stats}")

# 6. Age distribution (Identify if fraud patterns relate to age groups)
age_distribution = df['Age'].describe()
print(f"\nAge distribution:\n{age_distribution}")

# 7. Check for users with multiple email addresses (potential fraud flag)
multiple_email_users = df[df['has_email'] == 1]['email'].value_counts().loc[lambda x: x > 1]
print(f"\nUsers with multiple email addresses:\n{multiple_email_users}")

# 8. Average closing balance (could be useful for financial insights)
avg_closing_balance = df['avg_closing_balance'].mean()
print(f"\nAverage closing balance: {avg_closing_balance:.2f}")

# 9. Province/City fraud hotspots (to identify risky regions)
province_distribution = df['Province'].value_counts()
city_distribution = df['City'].value_counts()
print(f"\nFraud hotspots by province:\n{province_distribution}")
print(f"\nFraud hotspots by city:\n{city_distribution}")

