import pandas as pd
df = pd.DataFrame({
    "A": ['Tom', 'Nick', 'John', 'Peter'],
    "B": [15, 26, 17, 28]
})

res = df.copy()
res.columns = ["Col_1", "Col_2"]
res.index = ["R_1", "R_2", "R_3", "R_4"]
print(res)