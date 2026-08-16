import pandas as pd

# print(pd.__version__)

# Pandas is a Python library used for working with, cleaning, analyzing, and manipulating data.
## Series is essentially a one-dimensional labeled data structure.

data = [100, 101, 102.5]
dataString = ["A", "B", "C", "D"]

series = pd.Series(data)
# print(series)

series2 = pd.Series(dataString, index=["a", "b", "c", "d"])
# print(series2)

# print(series.loc[0])
# print(series[[0, 2]])
# print(series.iloc[0])

# series.loc[0] = 200
# print(series.loc[0])

# print(series2.loc["a"])
# print(series2.iloc[0])


datas = [100, 101, 102, 103, 200, 300]

datasSeries = pd.Series(datas, index=["a", "b", "c", "d", "e", "f"])
# print(datasSeries)
# print(datasSeries[["a", "b", "c"]])

# print(datasSeries[datasSeries > 200])
# print(datasSeries[datasSeries % 2 == 0])


calories = {"Day 1":1700, "Day 2":2300, "Day 3":1800}

caloriesSeries = pd.Series(calories)
print(caloriesSeries)
print(caloriesSeries["Day 1"])

caloriesSeries["Day 4"] = 2000
caloriesSeries["Day 3"] = 1900

print(caloriesSeries)
print(caloriesSeries[caloriesSeries > 2000])

