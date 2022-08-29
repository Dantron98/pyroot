import uproot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
file = uproot.open('/home/wexon/PyRoot/PoQ02-16.875-18.625.root')
t = file['Shower;1']
x = np.array([])
y = np.array([])
for entry in t:
    xmax = t['Xmax']
    lgE = t['lgE']
    x = np.append(x, lgE)
    y = np.append(y, xmax)
xnew = pd.DataFrame(x, columns=['lgE'])
ynew = pd.DataFrame(y, columns=['Xmax'])
df = xnew.join(ynew)
df = df[df['Xmax'] < 1100][['Xmax', 'lgE']].round(5)
lge_unic = df['lgE'].unique()
long = len(lge_unic)
ymin = np.array([])
ymax = np.array([])
for i in range(long):
    test = lge_unic[i]
    ymin = np.append(ymin, df.loc[df['lgE'] == test, 'Xmax'].min())
    ymax = np.append(ymin, df.loc[df['lgE'] == test, 'Xmax'].max())
#x_train, x_test, y_train, y_test = train_test_split(lge_unic, ymin, test_size=0.4, random_state=101)
lm = LinearRegression()
lm.fit(lge_unic.reshape(-1,1), ymin)
predictions = lm.predict(lge_unic)
plt.plot(predictions, ymin)
plt.figure(figsize=(8,5), dpi=300)
plt.xlabel('lgE')
plt.ylabel('Xmax')
plt.plot(df['lgE'],df['Xmax'], 'ro')
plt.grid(True)
plt.show()