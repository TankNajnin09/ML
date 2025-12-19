import pandas as pd

# Two-dimensional list
data = [
    [1, 'Asha', 85],
    [2, 'Krisha', 90],
    [3, 'Himali', 88]
]

# Create DataFrame
df = pd.DataFrame(data, columns=['ID', 'Name', 'Marks'])

# Display DataFrame
print(df)
