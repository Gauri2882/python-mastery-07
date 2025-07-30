""" Customizing graphs """

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# plot
plt.plot(x, y, label = "Line", color = "green", linestyle = ":", marker = "o")
plt.title("Customized line graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.annotate("Max Value", xy = (5, 10), xytext = (4.5, 8),
             arrowprops= dict(facecolor = 'black', arrowstyle = '->'))
plt.legend()
plt.show()

# subplot
x1 = [1, 2, 4, 5, 6]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 3, 4, 5]

# subplots
plt.subplot(1, 2, 1)
plt.plot(x1, y1, color = "blue")
plt.title("Graph 1")

plt.subplot(1, 2, 2)
plt.plot(x1, y2, color = "red")
plt.title("Graph 2")

# plt.tight_layout()
plt.show()

