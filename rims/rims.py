#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
df = pd.read_csv("20240914Loc1-3_SK.csv")
data = np.array(df["nd"])


bin_width = 0.001
bins = np.arange(1.490, 1.510+bin_width, bin_width)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(data, bins=bins, histtype="bar", edgecolor="black", color="blue")

#軸の設定
plt.xlabel("Refractive index (nd)")
plt.ylabel("Number of grains")
ax.set_ylim(0, 30)
xticks = np.arange(1.490, 1.510, 0.005)
plt.xticks(xticks, [f"{x:.3f}" for x in xticks])

plt.savefig("SK_ash.png")
plt.show()
# %%
