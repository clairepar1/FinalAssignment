import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Healthcare - Case Studies 3  country population growth rate 2016-2019.csv")

#Most popular item sold based on zip code
df["zip_code"] = df ["zip_code"].astype(int)
bottle_per_zip = df.groupby(["zip_code"])["bottles_sold"].max().sort_values(ascending=False)
plt.scatter(bottle_per_zip.index, bottle_per_zip, c=np.random.rand(len(bottle_per_zip),3))
plt.title("Most popular item sold based on zip code")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.show()

#Percentage of sales per store
total = df["sale_dollars"].sum()
df["percentage"] = (df["sale_dollars"]*100) / total
total_percentage = df.groupby(["store_name"])["percentage"].sum().sort_values(ascending=False)
#print(total_percentage)
#print(df[["store_number","percentage"]])
plt.scatter(total_percentage, total_percentage.index, c=np.random.rand(len(total_percentage),3))
plt.yticks(fontsize=6)
plt.xlabel("Percentage of sales")
plt.ylabel("Store name")
plt.title("Percentage of sales per store")
plt.show()
