import pandas as pd
from collections import Counter

# Load the Excel file
file_path = 'FTDH User Data.xlsx'
df = pd.read_excel(file_path)

# ----------------------- #
# Step 1: Extract the 'email' column and drop NaN values
# ----------------------- #
email_data = df['email'].dropna().astype(str)

# ----------------------- #
# Step 2: Count the occurrences of each email
# ----------------------- #
email_counts = Counter(email_data)

# Get the 5 most common emails
most_common_emails = email_counts.most_common(5)

# ----------------------- #
# Step 3: Print the 5 most common emails and their counts
# ----------------------- #
print("Most common emails:")
for email, count in most_common_emails:
    print(f"{email}: {count}")
