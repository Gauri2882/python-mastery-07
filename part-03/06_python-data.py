""" Creating basic plot """

import matplotlib.pyplot as plt

x = [1, 2, 3, 5, 8]
y = [2, 4, 6, 8, 9]

# plot 
plt.plot(x, y, label = "Line")
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# bar chart
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 30]

# plot
plt.bar(categories, values, color = "skyblue")
plt.title("Bar chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()
plt.show()

# scatter plot
x  = [1, 2, 3, 4, 6]
y = [2.5, 3.7, 4.6, 8.0, 10.5]

# plot
plt.scatter(x, y, color = "red")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()