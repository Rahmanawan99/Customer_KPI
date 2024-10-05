import pandas as pd

# Load the Excel file
file_path = 'FTDH User list 2024-09-27.xlsx'
df = pd.read_excel(file_path)

# ----------------------- #
# Step 1: Extract the last 3 words from the 'IRIS Address' column
# ----------------------- #

# Define a function to extract the last 3 words
def extract_city_name(address):
    # Split the address into words
    words = str(address).split()
    
    # Check if there are at least 3 words
    if len(words) >= 3:
        # Return the last 3 words joined together
        return ' '.join(words[-3:])
    else:
        return None  # Return None if there are less than 3 words

# Apply the function to the 'IRIS Address' column and create a new column 'City Name'
df['City Name'] = df['IRIS Address'].apply(extract_city_name)

# ----------------------- #
# Step 2: Save only the 'City Name' column to a new CSV file
# ----------------------- #

# Create a DataFrame with just the 'City Name' column
city_names_df = df[['City Name']]

# Save the result to a new CSV file
output_file_path = 'City_Names.csv'
city_names_df.to_csv(output_file_path, index=False)

print(f"City names saved to {output_file_path}")
