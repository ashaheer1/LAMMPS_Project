# Looking at min box 2-8 convergence to see how minimization converged. Plotting Potential Energy PotEng vs Step to see their convergence. 
# block_labels.csv shows what each block did in minimization.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
import os
import re

files = sorted(glob.glob("extracted/min_box_block[3-8].csv"))
df_block2 = pd.read_csv("extracted/min_box_block2.csv")
#files = sorted(glob.glob("extracted/min_box_block[3-4].csv"))
label = pd.read_csv("extracted/block_labels.csv")

dfs = []
df_block2['filename'] = 'min_box_block2' 

for file in files:
    df = pd.read_csv(file)
    #print(df)
    name = os.path.splitext(os.path.basename(file))[0]
    
    df['filename'] = name
    dfs.append(df)

#print(dfs)

#Getting their description from block_labels.csv

def get_label(name):
    m = re.match(r"(.+)_block(\d+)$", name)
    if not m:
        return name
    f, b = m.group(1), int(m.group(2))
    row = label[(label.file == f) & (label.block == b)]
    return row.description.iloc[0] if not row.empty else name

#print(get_label(name))

fig, ax = plt.subplots(2, 3, figsize=(16,7))

#fig, ax = plt.subplots(1, 2, figsize=(16,7))

ax = ax.flatten()

for i, df in enumerate(dfs): 
    ax[i].plot(df['Step'], df['PotEng'], '-.', label='Potential Energy', color='Blue')
    name = df['filename'].iloc[0]    
    ax[i].set_title(get_label(name)) 
    ax[i].ticklabel_format(axis='x', style='plain', useOffset=False)
    ax[i].ticklabel_format(axis='y', style='plain', useOffset=False)
    #ax[i].set_xlabel('Step')
    #ax[i].set_ylabel('Potential Energy')
    ax[i].legend()
    ax[i].grid(alpha=0.4)
    fig.supxlabel('Step')
    fig.supylabel('Potential Energy')


#plt.scatter(df['Step'], df['PotEng'])
#print(df_block2)

plt.tight_layout()
plt.savefig(f'plots/curated_plots/Min_Box_Convergence_Plots.png', dpi=150)

plt.figure(2)
plt.plot(df_block2['Step'], df_block2['TotEng'],'-.', label='Total Energy', color='Red')
plt.xlabel('Step')
plt.ylabel('Energy')
plt.title(get_label(df_block2['filename'].iloc[0]))
plt.legend()
plt.grid(alpha=0.4)
#plt.show()
plt.savefig(f'plots/curated_plots/Min_Box_Atom_Min_Convergence_Plot.png', dpi=150)

