# Import numpy
import numpy as np

# Sample dataset (rows = samples, columns = features)
data = np.array([[10, 200, 30],
                 [15, 300, 25],
                 [20, 400, 35],
                 [25, 500, 40]])

print("Original Data:")
print(data)

# Step 1: Calculate mean of each feature (column)
mean_values = np.mean(data, axis=0)
print("\nMean of each feature:")
print(mean_values)

# Step 2: Perform mean removal (mean centering)
mean_removed_data = data - mean_values

print("\nData after Mean Removal:")
print(mean_removed_data)
