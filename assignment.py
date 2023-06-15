import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Healthcare - Case Studies 3  country population growth rate 2016-2019.csv")

df["zip_code"] = df ["zip_code"].astype(int)
bottle_per_zip = df.groupby(["zip_code"])["bottles_sold"].max().sort_values(ascending=False)

plt.scatter(bottle_per_zip.index, bottle_per_zip, c=np.random.rand(len(bottle_per_zip),3))
plt.title("Bottles Sold")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.show()