import pandas as pd

df = pd.read_json("colors.json")

print(df.to_string())