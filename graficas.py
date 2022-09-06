import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.interpolate import  interp1d
file = pd.read_csv('/home/wexon/software/congreso/PoQ02.csv')
g = sns.FacetGrid(data=file)
g = sns.relplot(x=file['lgE'], y=file['Xmax'], data=file, palette='coolwarm')
x = np.array(file['lgE'])
y = np.array(file['Xmax'])
coeficiente = np.polyfit(x, y, 1)
polinomio = np.poly1d(coeficiente)
f = interp1d(x, y, 1)
ys = polinomio(x)
plt.plot(x, ys, 'r')
g1 = sns.displot(file['Xmax'], kde=True)
g2 = sns.displot(file['lgE'], kde=True)
g3 = sns.jointplot(x=file['lgE'], y=file['Xmax'], data=file)
g4 = sns.lmplot(x='lgE', y='Xmax', data=file,  line_kws={'color': 'r'})
plt.show()