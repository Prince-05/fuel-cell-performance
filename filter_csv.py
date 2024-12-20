import pandas as pd

# Path to the dataset
file_path = 'Fuel_cell_performance_data-Full.csv'  # Update with the correct path if needed

# Load the dataset
data = pd.read_csv(file_path)

# Inspect column names
print("Columns in the dataset:")
print(data.columns)

# Drop all target columns except 'target_5'
columns_to_drop = [col for col in data.columns if col.startswith('Target') and col != 'Target5']
data_cleaned = data.drop(columns=columns_to_drop)

# Verify the remaining columns
print("Columns after dropping unnecessary targets:")
print(data_cleaned.columns)

# Save the cleaned dataset
data_cleaned.to_csv('Filtered_Fuel_cell_performance_data.csv', index=False)
print("Cleaned dataset saved as 'Fuel_cell_performance_data_cleaned.csv'.")
