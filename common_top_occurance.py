import pandas as pd
from collections import Counter

# Load the Excel file
file_path = 'FTDH User list 2024-09-27.xlsx'
df = pd.read_excel(file_path)

# ----------------------- #
# Step 1: Count the occurrences of full names
# ----------------------- #

# Drop NaN values and count the frequency of each full name
full_name_counts = Counter(df['IRIS Address'].dropna().astype(str))

# Get the 5 most common full names
most_common_full_names = full_name_counts.most_common(10)

# Print the 5 most common full names
print("Top 5 most common full names in the IRIS Address column:")
for name, count in most_common_full_names:
    print(f"{name}: {count}")
