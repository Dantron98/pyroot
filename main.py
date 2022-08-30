import uproot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import  interp1d
file = uproot.open('/home/wexon/PyRoot/PoQ02-16.875-18.625.root')
file2 = uproot.open('/home/wexon/PyRoot/Fe.root')
t = file['Shower;1']
t2 = file2['Shower;1']
x = np.array([])
y = np.array([])
x2 = np.array([])
y2 = np.array([])

for entry in t:
    xmax = t['Xmax']
    lgE = t['lgE']
    x = np.append(x, lgE)
    y = np.append(y, xmax)
xnew = pd.DataFrame(x, columns=['lgE'])
ynew = pd.DataFrame(y, columns=['Xmax'])

for entry in t2:
    xmax = t2['Xmax']
    lgE = t2['lgE']
    x2 = np.append(x2, lgE)
    y2 = np.append(y2, xmax)

x2new = pd.DataFrame(x2, columns=['lgE'])
y2new = pd.DataFrame(y2, columns=['Xmax'])
df = xnew.join(ynew)
df2 = x2new.join(y2new)
df = df[df['Xmax'] < 1100][['Xmax', 'lgE']].round(5)

x = np.array(df['lgE'])
y = np.array(df['Xmax'])
df.to_csv('/home/wexon/software/congreso/PoQ02.csv')
df2.to_csv('/home/wexon/software/congreso/Fe.csv')

coeficiente = np.polyfit(x, y, 1)
polinomio = np.poly1d(coeficiente)
f = interp1d(x, y, 1)
ys = polinomio(x)
fig = plt.figure()
plt.title('Grafica 1')
plt.plot(df2['lgE'], df2['Xmax'], 'o', label='Datos PoQ02')
plt.grid(True)
plt.xlabel('lgE')
plt.ylabel('Xmax')
print(polinomio)
#plt.plot(x, ys, label='ajuste')
plt.show()