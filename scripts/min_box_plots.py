# Looking at min boxes 3-5 with Pressure sepcified to LAMMPS. Checking if the targeted pressures (x and y) are achieved by LAMMPS at different conditions.
# Block 3 is isotropic meaning properties are same in both x and y directions.
# Block 4 is anisotropic meaning properties of the box can change different between x and y direction.
# Block 5 specified the pressure in x-direction as 1.0 and y-diection as 2.0.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #Needs matplotlib > 3.11 check using print(matplotlib.__version__)
import os
import glob

files = sorted(glob.glob("extracted/min_box_block[3-5].csv"))

last_row = []

for file in files:
    df = pd.read_csv(file)
    #print(df)
    df_last = df.iloc[-1].copy()
    df_last['filename'] = os.path.basename(file)

    last_row.append(df_last)
    
tog = pd.DataFrame(last_row)

P3 = [1.5, 1.5]
P4 = [1.5, 1.5]
P5 = [1.0, 2.0]

targets = [P3, P4, P5]

targ_x = [p[0] for p in targets]
targ_y = [p[1] for p in targets]

Pxx_ach = tog['Pxx'].tolist()
Pyy_ach = tog['Pyy'].tolist()

#print(tog)

Block_label = ["Block 3", "Block 4", "Block 5"]

# --------- Doing Convergence Plot Now ------------------

dfs = []

for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

#for df in dfs:
#    print(df)

# --------- Convergence Plot of Pressures ----------------

#fig, ax = plt.subplots(1, 2, figsize=(12, 5))
#ax[0].plot(dfs[1]['Step'], dfs[1]['Pxx'], label='Pxx')
#ax[0].axhline(y=P3[0], color='Red', linestyle='--', label='Target')
#ax[0].set_xlabel('Step')
#ax[0].set_ylabel('Pressure Pxx')
#ax[0].set_title('Block 3: Pxx Convergence')
#ax[0].legend()
#ax[0].grid(alpha=0.4)

#ax[1].plot(dfs[1]['Step'], dfs[1]['Pyy'], label='Pyy')
#ax[1].axhline(y=P3[1], color='Red', linestyle='--', label='Target')
#ax[1].set_xlabel('Step')
#ax[1].set_ylabel('Pressure Pyy')
#ax[1].set_title('Block 3: Pyy Convergence')
#ax[1].legend()
#ax[1].grid(alpha=0.4)

for i, df in enumerate(dfs):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].plot(df['Step'], df['Pxx'], label='Achieved Pxx')
    ax[0].axhline(y=targets[i][0], color='Red', linestyle='--', label='Target Pxx')
    ax[0].set_xlabel('Step')
    ax[0].set_ylabel('Pressure Pxx')
    ax[0].set_title(f'Block {i+3}: Pxx Convergence')
    ax[0].legend()
    ax[0].grid(alpha=0.4)

    ax[1].plot(df['Step'], df['Pyy'], label='Achieved Pyy') 
    ax[1].axhline(y=targets[i][1], color='Red', linestyle='--', label='Target Pyy')
    ax[1].set_xlabel('Step')
    ax[1].set_ylabel('Pressure Pyy')
    ax[1].set_title(f'Block {i+3}: Pyy Convergence')
    ax[1].legend()
    ax[1].grid(alpha=0.4)

    ax[0].ticklabel_format(axis='x', style='plain', useOffset=False)
    ax[1].ticklabel_format(axis='x', style='plain', useOffset=False)
    #plt.show()
    plt.savefig(f'plots/curated_plots/Block_{i+3}_Pressure_Convergence_Plots.png', dpi=150)
# -------- Bar Plots for Block 3-5 -----------------------------
fig, ax = plt.subplots(1,2, figsize=(14, 5))

bar_xx = ax[0].grouped_bar([targ_x, Pxx_ach], tick_labels=Block_label, labels=['Target','Achieved'])
ax[0].set_title('Pxx')
ax[0].set_ylabel('Pressure')
ax[0].legend()

ax[0].bar_label(
        bar_xx.bar_containers[0],
        labels=[f"{v:.3f}" for v in targ_x], padding=2)

ax[0].bar_label(
        bar_xx.bar_containers[1],
        labels=[f"{v:.3f}" for v in tog['Pxx']], padding=2)

bar_yy = ax[1].grouped_bar([targ_y, Pyy_ach], tick_labels=Block_label, labels=['Target','Achieved'])
ax[1].set_title('Pyy')
ax[1].set_ylabel('Pressure')
ax[1].legend()
ax[1].bar_label(bar_yy.bar_containers[0],
                labels=[f'{v:0.3f}' for v in targ_y], padding=2)
ax[1].bar_label(bar_yy.bar_containers[1],
                labels=[f'{v:0.3f}' for v in tog['Pyy']], padding=2)



#plt.grouped_bar(tog['Pxx']
ax[0].grid(alpha=0.4)
ax[1].grid(alpha=0.4)
plt.savefig(f'plots/curated_plots/Block3-5_Pressures_Min_Box_Bar_Plot.png', dpi=150)
#plt.show()

