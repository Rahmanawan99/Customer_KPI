import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Word CLoud, can be applied to any non-numeric column

# Load the file
file_path = 'FTDH User list 2024-09-27.xlsx'
df = pd.read_excel(file_path)

# Extract words from full_name

# Join all the name/addess or any data into a single string
text = ' '.join(df['IRIS Address'].dropna().astype(str))

# Generate the Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)

# Visualize the Word Cloud
# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # No axes for the word cloud
plt.title('Word Cloud of Full Names', fontsize=16)  # Complete title
plt.show()
