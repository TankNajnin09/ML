import pandas as pd

# Two-dimensional list
data = [
    [101, "Asha", 78],
    [102, "Krisha", 85],
    [103, "Himali", 90]
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Roll No", "Name", "Marks"])

# Display DataFrame
print(df)
