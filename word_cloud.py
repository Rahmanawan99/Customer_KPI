import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'FTDH User list 2024-09-27.xlsx'
df = pd.read_excel(file_path)

# ----------------------- #
# Step 1: Extract words from full_name
# ----------------------- #

# Join all full names into a single string
text = ' '.join(df['IRIS Address'].dropna().astype(str))

# ----------------------- #
# Step 2: Generate the Word Cloud
# ----------------------- #

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)

# ----------------------- #
# Step 3: Visualize the Word Cloud
# ----------------------- #

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # No axes for the word cloud
plt.title('Word Cloud of Full Names', fontsize=16)  # Complete title
plt.show()
