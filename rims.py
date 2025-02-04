#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./rims/20240914Loc1-3_SK.csv")
data = np.array(df["nd"])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(data, bins=10, histtype="barstacked", ec="black")
plt.xlabel("Reflective index (nd)")
plt.ylabel("Number of grains")

plt.show()
# %%
