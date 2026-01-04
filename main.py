import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Penguins Data (1).csv')
print(data.head())
print(data.info())
sns.histplot(data['Culmen Length (mm)'])
plt.show()
sns.histplot(data['Culmen Depth (mm)'])
plt.show()
sns.histplot(data['Flipper Length (mm)'])
plt.show()
sns.histplot(data['Body Mass (g)'])
plt.show()
