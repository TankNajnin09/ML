# Import necessary libraries
import numpy as np

# Sample dataset
data = np.array([[10, 200],
                 [15, 300],
                 [20, 400],
                 [25, 500]])

print("Original Data:")
print(data)


# Function to normalize data
def normalize(data):
    # Calculate min and max for each column
    min_vals = data.min(axis=0)
    max_vals = data.max(axis=0)

    # Apply normalization formula
    normalized_data = (data - min_vals) / (max_vals - min_vals)
    return normalized_data


# Perform normalization
normalized_data = normalize(data)

print("\nNormalized Data:")
print(normalized_data)
