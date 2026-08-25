import pandas as pd

df = pd.read_csv("currency.csv", index_col="Code")
# df = pd.read_csv("currency.csv")


# print(df)

# print(df.to_string())

#### selection by column

# print(df["Name"])
# print(df["Name"][0])

# print(df["Name"].to_string())

# print(df[["Name", "Code"]].to_string())


#### Selction by rows

# print(df.to_string())

# print(df.loc[0])

# print(df.loc["AED"])

# print(df.loc["AED", ["Name"]])

# print(df.loc["AED":"INR", ["Name"]])  # Slicing the row

# print(df.iloc[0])   # selecting row based on rows

# print(df.iloc[0:9]) # doing the slicing using index

# print(df.iloc[0:10:2, 2]) # Slicing and then getting the specific column

# print(df.iloc[0:10:2, 0:3])


code = input("Enter a code??")

try:
    print(df.loc[code])
except KeyError:
    print(KeyError)

