# Program 46: Write a program to create a DataFrame from CSV or Excel files.
import pandas as pd
data = {"Name": ["Amit", "Riya"], "Marks": [80, 90]}
df = pd.DataFrame(data)
df.to_csv("marks.csv", index=False)
new_df = pd.read_csv("marks.csv")
print(new_df)
