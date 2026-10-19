# Program 48: Write a program to plot line, bar, histogram and pie charts using Python.
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [10, 20, 15]
plt.plot(x, y)
plt.title("Line Chart")
plt.show()
print("Line chart displayed")
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()
print("Bar chart displayed")
plt.hist(y)
plt.title("Histogram")
plt.show()
print("Histogram displayed")
plt.pie(y)
plt.title("Pie Chart")
plt.show()
print("Pie chart displayed")
