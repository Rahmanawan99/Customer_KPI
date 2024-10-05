import pandas as pd
from collections import Counter

# Load the city names CSV file
file_path = 'City_Names.csv'
df = pd.read_csv(file_path)

# Drop any NaN values in the 'City Name' column
df = df.dropna(subset=['City Name'])

# ----------------------- #
# Step 1: Top 10 most repeated cities
# ----------------------- #

# Count the occurrences of each city
city_counts = Counter(df['City Name'])

# Get the top 10 most common cities
top_10_cities = city_counts.most_common(10)

print("Top 10 most repeated cities:")
for city, count in top_10_cities:
    print(f"{city}: {count}")

# ----------------------- #
# Step 2: Number of unique cities
# ----------------------- #

unique_cities = len(city_counts)
print(f"\nNumber of unique cities: {unique_cities}")

# ----------------------- #
# Step 3: Most repeated city
# ----------------------- #

most_repeated_city = city_counts.most_common(1)
print(f"\nMost repeated city: {most_repeated_city[0][0]} with {most_repeated_city[0][1]} occurrences")

# ----------------------- #
# Step 4: Number of cities that appear only once
# ----------------------- #

# Filter the cities that appear only once
cities_appearing_once = [city for city, count in city_counts.items() if count == 1]
count_unique_cities_once = len(cities_appearing_once)

print(f"\nNumber of cities that appear only once: {count_unique_cities_once}")

# ----------------------- #
# Step 5: Visualization (Optional)
# ----------------------- #

import matplotlib.pyplot as plt

# Separate the cities and their counts
labels, counts = zip(*top_10_cities)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.barh(labels, counts, color='skyblue')
plt.xlabel('Count', fontsize=12)
plt.ylabel('City', fontsize=12)
plt.title('Top 10 Most Repeated Cities', fontsize=16)
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.tight_layout()

# Show the plot
plt.show()
