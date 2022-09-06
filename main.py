import uproot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import  interp1d
file = uproot.open('/home/wexon/PyRoot/PoQ02-16.875-18.625.root')['Shower;1']
file2 = uproot.open('/home/wexon/PyRoot/Fe.root')
lgE = pd.DataFrame(file['lgE'].array(library='pd'))
Xmax = pd.DataFrame(file['Xmax'].array(library='pd'))
lgE.columns = ['lgE']
Xmax.columns = ['Xmax']
df = lgE.join(Xmax)
df = df[df['Xmax'] < 1100][['Xmax', 'lgE']].round(5)

x = np.array(df['lgE'])
y = np.array(df['Xmax'])
print(df)
df.to_csv('/home/wexon/software/congreso/PoQ02.csv')
#df2.to_csv('/home/wexon/software/congreso/Fe.csv')

coeficiente = np.polyfit(x, y, 1)
polinomio = np.poly1d(coeficiente)
f = interp1d(x, y, 1)
ys = polinomio(x)
fig = plt.figure()
plt.title('Grafica 1')
plt.plot(df['lgE'], df['Xmax'], 'o', label='Datos PoQ02')
plt.grid(True)
plt.xlabel('lgE')
plt.ylabel('Xmax')
print(polinomio)
plt.plot(x, ys, label='ajuste')
plt.show()