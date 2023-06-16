import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Healthcare - Case Studies 3  country population growth rate 2016-2019.csv")
"""
#Most popular item sold based on zip code
df["zip_code"] = df ["zip_code"].astype(int)
bottle_per_zip = df.groupby(["zip_code"])["bottles_sold"].max().sort_values(ascending=False)
plt.scatter(bottle_per_zip.index, bottle_per_zip, c=np.random.rand(len(bottle_per_zip),3))
plt.title("Bottles Sold")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.show()
"""
#Percentage of sales per store
#print(df["sale_dollars"],df["store_name"])
total = df["sale_dollars"].sum()

df['percentage'] = (df['sale_dollars']*100) / total
print(df[['store_number','percentage']])
