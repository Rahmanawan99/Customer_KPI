import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

#IN THIS CODE AGAIN YOU CAN MAKE A COLUMN/BAR CHART FOR ANY FIELD, HERE I DID device_count

# Load the file
file_path = 'FTDH User Data.xlsx'
df = pd.read_excel(file_path)

# Convert 'device_count' to numeric
df['device_count'] = pd.to_numeric(df['device_count'], errors='coerce')

# Drop NaN values from 'device_count'
device_count = df['device_count'].dropna()

# Count the frequency of each device count value
device_count_counts = device_count.value_counts().sort_index()

# Calculate statistics
mean = device_count.mean()
std_dev = device_count.std()
max_age = device_count.max()
min_age = device_count.min()

print(f"Mean device_count: {mean:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Max device_count: {max_age:.2f}")
print(f"Min device_count: {min_age:.2f}")

# Plot the column chart
plt.figure(figsize=(10, 6))
device_count_counts.plot(kind='bar', color='skyblue')

# Overlay the normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'r', linewidth=2, label='Normal Distribution (PDF)')

# Customize the plot
plt.title('Distribution of Device Count', fontsize=16)
plt.xlabel('Device Count', fontsize=10)
plt.ylabel('Number of Users', fontsize=12)
plt.xticks(rotation=0)  # Keep the x labels horizontal
plt.tight_layout()

# Display stats on the plot
plt.text(xmax*0.6, max(p)*0.8, f'Mean: {mean:.2f}\nStd Dev: {std_dev:.2f}\nMax device count: {max_age:.2f}\nMin device count: {min_age:.2f}', 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.5))


# Show the plot
plt.show()