import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = 'FTDH User Data.xlsx'
df = pd.read_excel(file_path)

# ----------------------- #
# Part 2: Correlation Matrix for Numerical Columns
# ----------------------- #

# Convert relevant columns to numeric if necessary
df['Days till FTDH'] = pd.to_numeric(df['Days till FTDH'], errors='coerce')
df['device_count'] = pd.to_numeric(df['device_count'], errors='coerce')
df['avg_closing_balance'] = pd.to_numeric(df['avg_closing_balance'], errors='coerce')

# Drop NaN values (optional, but ensures clean data for correlation)
df_clean = df[['Days till FTDH', 'device_count', 'avg_closing_balance']].dropna()

# Calculate the correlation matrix
corr_matrix = df_clean.corr()

# Print the correlation matrix
print("\nCorrelation Matrix:")
print(corr_matrix)

# ----------------------- #
# Part 3: Plot the Correlation Matrix
# ----------------------- #

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Key Features')
plt.tight_layout()

# Show the plot
plt.show()