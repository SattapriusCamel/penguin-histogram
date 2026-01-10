import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Penguins Data (1).csv')
print(df.head())
print(df.info())
sns.scatterplot(data = df,x = 'Culmen Length (mm)', y = 'Body Mass (g)', hue = 'Species')
plt.show()
sns.scatterplot(data = df,x = 'Culmen Depth (mm)', y = 'Body Mass (g)', hue = 'Species')
plt.show()
sns.pairplot(data=df, hue='Species')
plt.show()