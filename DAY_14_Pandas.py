import numpy as np 
import pandas as pd
l1 = [1, 2, 3, 4, 5, 6]
labels = ['a', 'b', 'c', 'd', 'e', 'f']
d1 = {"A":10, "B":20, "C":30, "D":40, "E":50}
s1 = pd.Series(l1)
print(s1)
print(s1[5])
s2 = pd.Series(labels)
print(s2)
print(s2[4])
s3= pd.Series(data=l1, index=labels)
print(s3)
print(s3["e"])
arr = np.random.randint(low= 1, high = 100 , size= (5,4))
print(arr)
print(type(arr))
print(pd.DataFrame(arr))
df = pd.DataFrame(arr, index = ["A", "B", "C", "D", "E"], columns= ["D", "U", "B", "A"])
print(df)
print(type(df))
print(df["U"])
print(df.loc["D"])
print(df[["D","B", "A"]])
print(df.iloc[3])
print(np.__version__ )
print(pd.__version__)
print(df.iloc[2])
df['Bird'] = [10,20,30,40,50]
print(df)
print(df.drop('Bird', axis = 1))
df.drop('B', axis = 1, inplace = True)
print(df)
print((df['U'] % 2 == 0) & (df['D'] % 2 == 0))




import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'Value': [5, 7, 8, 6, 10, 15, 13]}
df = pd.DataFrame(data)

# Plot
df.plot(x='Year', y='Value', kind='line', marker='o', linestyle='--', color='b')
plt.title("Line Plot of Values Over Years")
plt.xlabel("Year")
plt.ylabel("Value")
plt.grid()
plt.show()




import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 20, 15, 30]}
df = pd.DataFrame(data)

# Plot
df.plot(x='Category', y='Value', kind='bar', color='skyblue', legend=False)
plt.title("Bar Chart of Categories")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()





import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [25, 35, 20, 20]}
df = pd.DataFrame(data)

# Plot
df.set_index('Category').plot(kind='pie', y='Value', autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Pie Chart Example")
plt.ylabel("")  # Remove default y-axis label
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {'X': [5, 7, 8, 5, 10, 15, 13, 18],
        'Y': [7, 8, 6, 5, 10, 12, 15, 17]}
df = pd.DataFrame(data)

# Plot
df.plot(kind='scatter', x='X', y='Y', color='purple')
plt.title("Scatter Plot of X vs Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
data = np.random.normal(0, 1, 1000)
df = pd.DataFrame(data, columns=['Value'])

# Plot
df['Value'].plot(kind='hist', bins=30, color='steelblue', edgecolor='black')
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
data = {'Set1': np.random.normal(0, 1, 100),
        'Set2': np.random.normal(0, 2, 100),
        'Set3': np.random.normal(0, 3, 100),
        'Set4': np.random.normal(0, 4, 100)}
df = pd.DataFrame(data)

# Plot
df.plot(kind='box', patch_artist=True)
plt.title("Box Plot of Different Distributions")
plt.xlabel("Dataset")
plt.ylabel("Values")
plt.show()





import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = np.random.rand(10, 10)
df = pd.DataFrame(data, columns=[f'Var{i}' for i in range(1, 11)])

# Plot
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap="YlGnBu")
plt.title("Heatmap of Random Data")
plt.show()



