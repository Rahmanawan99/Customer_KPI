import pandas as pd

# Load the file
file_path = 'FTDH User Data.xlsx'
df = pd.read_excel(file_path)

# Convert 'Days till FTDH' to numeric, if not already
df['Days till FTDH'] = pd.to_numeric(df['Days till FTDH'], errors='coerce')

# Drop NaN values from 'Days till FTDH'
days_ftdh = df['Days till FTDH'].dropna()

#Count the number of entries depending on your needs
count_less_than_7 = (days_ftdh < 7).sum()
count_less_than_14 = (days_ftdh < 14).sum()
count_less_than_30 = (days_ftdh < 30).sum()
count_less_than_60 = (days_ftdh < 60).sum()

# Print the count
print(f"Number of entries in 'Days till FTDH' less than 7: {count_less_than_7}")
print(f"Number of entries in 'Days till FTDH' less than 14: {count_less_than_14}")
print(f"Number of entries in 'Days till FTDH' less than 30: {count_less_than_30}")
print(f"Number of entries in 'Days till FTDH' less than 60: {count_less_than_60}")
