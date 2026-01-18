import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Penguins Data (1).csv')
print(data.isnull().sum())
data.hist()
plt.show()
sns.pairplot(data=data, hue = 'Species')
plt.legend()
plt.show()
#sns.heatmap(data.corr(), annot=True)
#plt.show()
data.plot(kind='box', subplots=True, layout=(5,3),figsize=(15,12))
plt.show() 
sns.countplot(x = 'Gender', data=data, hue='Species')
plt.show()