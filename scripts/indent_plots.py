#Plotting Temperature, Total Energy, Volume in indenter vs without indenter.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

ind = pd.read_csv("extracted/indent_block1.csv", usecols=["Step", "Temp", "TotEng", "Volume"])
nonind = pd.read_csv("extracted/indent_block2.csv", usecols=["Step", "Temp", "TotEng", "Volume"])
#Steps_nonind = pd.read_csv("extracted/indent_block2.csv", usecols=["Step"])

ind = ind.rename(columns={"Temp": "Temp_in", "TotEng": "TotEng_in", "Volume": "Volume_in"})

nonind = nonind.rename(columns={"Temp": "Temp_non", "TotEng": "TotEng_non", "Volume": "Volume_non"})

#combined = pd.concat([ind, nonind], axis=1)

plt.figure(1)
plt.scatter(ind['Step'], ind['Temp_in'], label='Indenter On', color='Blue')
plt.scatter(nonind['Step'], nonind['Temp_non'], label='Indenter Off', color='Orange')
plt.axvline(x=30000, linestyle='--', color='Red', alpha=0.3, label='Indenter Turned Off')
plt.title('Temperature Plot Indenter On/Off')
plt.xlabel('Steps')
plt.ylabel('Reduced LJ Temperature')
plt.grid(alpha=0.5)
plt.legend()
plt.savefig(f'plots/curated_plots/Indenter_On_Off_Temp_Plot.png', dpi=150)

plt.figure(2)
plt.scatter(ind['Step'], ind['TotEng_in'], label='Indenter On', color='Blue')
plt.scatter(nonind['Step'], nonind['TotEng_non'], label='Indenter Off', color='Orange')
plt.axvline(x=30000, linestyle='--', color='Red', alpha=0.3, label='Indenter Turned Off')
plt.title('Total Energy Plot Indenter On/Off')
plt.xlabel('Steps')
plt.ylabel('Total Energy ε')
plt.grid(alpha=0.5)
plt.legend()
plt.savefig(f'plots/curated_plots/Indenter_On_Off_TotEng_Plot.png', dpi=150)

plt.figure(3)
plt.scatter(ind['Step'], ind['Volume_in'], label='Indenter On', color='Blue')
plt.scatter(nonind['Step'], nonind['Volume_non'], label='Indenter Off', color='Orange')
plt.axvline(x=30000, linestyle='--', color='Red', alpha=0.3, label='Indenter Turned Off')
plt.title('Volume Plot Indenter On/Off')
plt.xlabel('Steps')
plt.ylabel('Volume')
plt.grid(alpha=0.5)
plt.legend()
plt.savefig(f'plots/curated_plots/Indenter_On_Off_Vol_Plot.png', dpi=150)


#plt.show()
