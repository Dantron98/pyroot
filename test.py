import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.interpolate import  interp1d
file = pd.read_csv('/home/wexon/software/congreso/PoQ02.csv')
file = file[['Xmax', 'lgE']]
step = 0.125
for i in range(file['lgE'].min, file['lgE'].max(), step):
    new_data = file[file['lgE'] < step]
    g = sns.displot(new_data['lgE'])
    plt.show()
