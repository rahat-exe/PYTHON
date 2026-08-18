import pandas as pd

data = {
    "name": ["Rahat", "MUKSID", "ABBASI"],
    "age": [23, 24, 25]
}

# df = pd.DataFrame({
#     "name": ["Rahat", "MUKSID", "ABBASI"],
#     "age": [23, 24, 25]
# })

df = pd.DataFrame(data)
# print(df)

# print(df.loc[0])

# add a new column
df["job"] = ["Developer", "designer", "N/A"]

# print(df)

# add a new row

newRow = pd.DataFrame({"name":["Sohel", "Changsrang"], "age":["24", "25"], "job":["N/A", "Hacker"]})

# print(newRow)

df = pd.concat([df, newRow])

print(df)