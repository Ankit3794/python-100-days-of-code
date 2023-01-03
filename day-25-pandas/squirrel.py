import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

df2 = data.groupby(["Primary Fur Color"])["Primary Fur Color"].count().reset_index(name="counts")

print(type(df2))
print(df2)


df3 = data.value_counts(subset=["Primary Fur Color"]).reset_index(name="Counts")
print(type(df3))
print(df3)
