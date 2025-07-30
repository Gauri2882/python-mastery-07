""" Plotting temprature trends """
""" Highlighting Anamolies and Averages """
""" Customizing and saving plots """


import pandas as pd
import matplotlib.pyplot as plt
import seaborn

# load temp data
data = pd.read_csv("part-05/temperature_data.csv")
print(data.head())

plt.style.use("seaborn-v0_8-darkgrid") # change style
plt.plot(data['Date'], data['Temperature'], label = "Daily Temperature", color = 'blue')
plt.title("Customized temperature plot")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.legend()
plt.savefig("temperature_plot.png") # save the plot
plt.show()

# identify anomalies
mean_temp = data['Temperature'].mean()
std_temp = data['Temperature'].std()
data['Anomaly'] = (data['Temperature'] > mean_temp + 2 * std_temp) | (data['Temperature'] < mean_temp - 2 * std_temp)

# plot with anomalies
plt.plot(data['Date'], data['Temperature'], label = "Daily Temperature")
plt.scatter(data[data['Anomaly']]['Date'], data[data['Anomaly']]['Temperature'], color = 'red', label = "Anomaly")
plt.title("Temperature trends with anomalies")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.grid(True)
plt.legend()
plt.show()

# plot temprature trend
plt.plot(data['Date'], data['Temperature'], label = "Temperature")
plt.title("Temperature Trends")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.legend()
plt.show()

# add rolling average column
data['7-Day Average'] = data['Temperature'].rolling(window = 7).mean()

# plot
plt.plot(data['Date'], data['7-Day Average'], label = "7-Day average", linestyle = "--")
plt.title("Temperature trends with rolling average")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.legend()
plt.show()
