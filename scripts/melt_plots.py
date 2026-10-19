#To make curated plots specific to melt example
# Looking at Temperature(Temp) and Total Energy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os
import re

#file = glob.glob("extracted/melt_block1.csv")

df = pd.read_csv("extracted/melt_block1.csv")

Temp = df['Temp']
TEng = df['TotEng']
Step = df['Step']

plt.figure(1)
#m,b = np.polyfit(Step, Temp, 1)
#plt.plot(Step, m*Step+b, color='Red', linestyle=':')
plt.plot(Step, Temp, '-.', color='Red')
plt.ylim(1,3.5)
plt.xlabel("Steps")
plt.ylabel("Temperature")
plt.title("Temperature Change as Material Melts")
plt.grid(alpha=0.5)
plt.savefig(f'plots/curated_plots/Melt_Temp_Plot.png', dpi=150)

plt.figure(2)
plt.plot(Step, TEng, '-.', color='Green')
plt.ylim(-3,-1)
plt.xlabel("Steps")
plt.ylabel("Total Energy")
plt.title("Total Energy of the System During Melt")
plt.grid(alpha=0.5)
plt.savefig(f'plots/curated_plots/Melt_TotEng_Plot.png', dpi=150)

#plt.show()
