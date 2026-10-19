# Program 45: Write a program to perform basic data analysis using Pandas DataFrame.
import pandas as pd
data = {"Name": ["Amit", "Riya", "Neha"], "Marks": [80, 90, 75]}
df = pd.DataFrame(data)
print(df)
print("Maximum marks :", df["Marks"].max())
print("Minimum marks :", df["Marks"].min())
