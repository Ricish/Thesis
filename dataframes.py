import pandas as pd
import json
import os

# Specify the output directory for the CSV files
output_dir = r"C:\Users\Rico Nicolaas\Pycharm Projects\Thesis\CSV Files"  # Replace with your desired directory path
delimiter = ","  # Change this to '\t' for tab or ';' for semicolon-separated values

# Load JSON lines file
with open('questions.jsonl') as f:
    question_data = [json.loads(line) for line in f]

# Extract unique source_ids
source_ids = set(entry['source_id'] for entry in question_data)

# Create DataFrames for each source_id
dataframes = {}
for source_id in source_ids:
    filtered_data = [entry for entry in question_data if entry['source_id'] == source_id]
    dataframes[source_id] = pd.DataFrame(filtered_data)

print(dataframes)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Save each DataFrame to a CSV file in the specified directory
for source_id, df in dataframes.items():
    file_path = os.path.join(output_dir, f"{source_id}.csv")
    df.to_csv(file_path, index=False, sep=delimiter)  # Specify the delimiter
    print(f"Saved {source_id} DataFrame to {file_path} with delimiter '{delimiter}'")

print("All DataFrames have been saved as CSV files.")

