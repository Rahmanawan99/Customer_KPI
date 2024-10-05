import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

#Normal distribution/Bell chart for numeric data

# Load the file
file_path = 'FTDH User Data.xlsx'
df = pd.read_excel(file_path)

# Convert to numeric if not already
df['device_count'] = pd.to_numeric(df['device_count'], errors='coerce')

# Drop NaN values 
days_ftdh = df['device_count'].dropna()

# Calculate statistics
mean = days_ftdh.mean()
std_dev = days_ftdh.std()
max_age = days_ftdh.max()
min_age = days_ftdh.min()

print(f"Mean device_count: {mean:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Max device_count: {max_age:.2f}")
print(f"Min device_count: {min_age:.2f}")


# Plot the histogram with a fitted normal distribution
plt.figure(figsize=(10, 6))
sns.histplot(days_ftdh, bins=30, kde=False, stat='density', color='skyblue', label='Age')

# Overlay the normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'r', linewidth=2, label='Normal Distribution (PDF)')

# Customize the plot
plt.title('Bell Curve: Device count Normal Distribution', fontsize=16)
plt.xlabel('Device count', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend()

# Display stats on the plot, this can vary based on the plot size, so change accordingly.
plt.text(xmax*0.6, max(p)*0.8, f'Mean: {mean:.2f}\nStd Dev: {std_dev:.2f}\nMax Age: {max_age:.2f}\nMin Age: {min_age:.2f}', 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()
