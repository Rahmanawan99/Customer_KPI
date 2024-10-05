import pandas as pd
from collections import Counter

#IN THIS CODE YOU CAN FIND TOP OCCURANCE OF ANY FIELD, NAME ADDRESS DATE ETC...

# Load the file
file_path = 'YOUR_FILE.xlsx'
df = pd.read_excel(file_path)


# Drop NaN values and count the frequency of each full name
field_counts = Counter(df['column_name'].dropna().astype(str))

# Get the 10 most common full names
most_common_field_counts = field_counts_counts.most_common(10)

# Print the 5 most common full names
print("Top 5 most common field_counts in the field:")
for name, count in most_common_field_counts:
    print(f"{name}: {count}")
