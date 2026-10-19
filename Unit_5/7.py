# Program 47: Write a program to handle missing data using dropna and fillna methods.
import pandas as pd
data = {"Name": ["Amit", "Riya", "Neha"], "Marks": [80, None, 75]}
df = pd.DataFrame(data)
print("Filled data:")
print(df.fillna(0))
print("Rows after dropna:")
print(df.dropna())
