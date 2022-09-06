import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
file = pd.read_csv('/home/wexon/software/congreso/PoQ02.csv')
file = file[['Xmax', 'lgE']]
cota_inf = 0
cota_sup = 17
for i in range(14):
    new_data = file[(file['lgE'] > cota_inf) & (file['lgE'] < cota_sup)]
    g = sns.displot(new_data['lgE'], kde=True)
    plt.show()
    cota_inf = cota_sup
    cota_sup = cota_sup + .125
