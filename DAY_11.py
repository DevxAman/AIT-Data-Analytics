import matplotlib.pyplot as plt

# Data
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
values = [5, 7, 8, 6, 10, 15, 13]

# Plot
plt.plot(years, values, marker='o', color='b', linestyle='--')
plt.title("Line Plot of Values Over Years")
plt.xlabel("Year")
plt.ylabel("Values")
plt.grid()
plt.show()



import matplotlib.pyplot as plt

# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 20, 15, 30]

# Plot
plt.bar(categories, values, color='skyblue')
plt.title("Bar Chart of Categories")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()



import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']
sizes = [25, 35, 20, 20]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Pie Chart Example")
plt.show()



import matplotlib.pyplot as plt

# Data
x = [5, 7, 8, 5, 10, 15, 13, 18]
y = [7, 8, 6, 5, 10, 12, 15, 17]

# Plot
plt.scatter(x, y, color='purple')
plt.title("Scatter Plot of X vs Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.random.normal(0, 1, 1000)

# Plot
plt.hist(data, bins=30, color='steelblue', edgecolor='black')
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()




import matplotlib.pyplot as plt
import numpy as np

# Data
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

# Plot
plt.boxplot(data, patch_artist=True)
plt.title("Box Plot of Different Distributions")
plt.xlabel("Dataset")
plt.ylabel("Values")
plt.show()




import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Data
data = np.random.rand(10, 10)

# Plot
sns.heatmap(data, annot=True, cmap="YlGnBu")
plt.title("Heatmap of Random Data")
plt.show()




