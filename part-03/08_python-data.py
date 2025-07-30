""" plotting from data files """

import pandas as pd
import matplotlib.pyplot as plt

#load data 
data = pd.read_csv("part-03/data.csv")

# plot
plt.plot(data["X"], data["Y"], label = "Data from CSV")
plt.title("Plot from CSV")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()