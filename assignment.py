import pandas as pd
df = pd.read_csv("Healthcare - Case Studies 3  country population growth rate 2016-2019.csv")

df['zip_code'] = df ['zip_code'].astype(int)
bottle_per_zip = df.groupby(["zip_code"])["bottles_sold"].max().sort_values(ascending=False)
print(bottle_per_zip)


