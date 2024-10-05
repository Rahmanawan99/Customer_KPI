import pandas as pd
from collections import Counter
import re

# Load the Excel file
file_path = 'FTDH User list 2024-09-27.xlsx'
df = pd.read_excel(file_path)

# ----------------------- #
# Step 1: Extract words and numbers from the 'address' column
# ----------------------- #

# Define a function to extract words and numbers from a string
def extract_words_numbers(text):
    # Extract words (alphanumeric characters) and numbers
    words = re.findall(r'\b\w+\b', str(text))  # \b is word boundary, \w+ is for word characters, including numbers
    return words

# Apply the function to the 'address' column
address_data = df['address'].dropna().astype(str).apply(extract_words_numbers)

# Flatten the list of lists into a single list of words/numbers
all_words_numbers = [item for sublist in address_data for item in sublist]

# ----------------------- #
# Step 2: Count the occurrences of words and numbers
# ----------------------- #

# Use Counter to count the frequency of each word/number
word_number_counts = Counter(all_words_numbers)

# Get the 5 most common words/numbers
most_common = word_number_counts.most_common(5)

# Print the 5 most common words/numbers
print("Most common words and numbers in the address column:")
for word, count in most_common:
    print(f"{word}: {count}")


# ----------------------- #
# Step 2: Count the occurrences of words and numbers
# ----------------------- #

# Use Counter to count the frequency of each word/number
word_number_counts = Counter(all_words_numbers)

# Get the 20 most common words/numbers
most_common = word_number_counts.most_common(20)

# Print the 20 most common words/numbers
print("Most common words and numbers in the address column:")
for word, count in most_common:
    print(f"{word}: {count}")

# ----------------------- #
# Step 3: Visualize the Most Common Words and Numbers (Optional)
# ----------------------- #

import matplotlib.pyplot as plt

# Separate the words and their counts
labels, counts = zip(*most_common)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.barh(labels, counts, color='skyblue')
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Words/Numbers', fontsize=12)
plt.title('Most Common Words and Numbers in Address Column', fontsize=16)
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.tight_layout()

# Show the plot
plt.show()
