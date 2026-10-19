# Seeing the Energy of the minimized system as it goes from no indenter to as the indenter pushes deeper.

# We know that block 1 has no indenter. 
# Block 2: indenter y=13
# Block 3: indenter y=12.5
# Block 4: indenter y=12
# Block 5: indenter y=11.4
# Block 6: indenter y=11.2
# Block 7: indenter y=11.0

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

files = sorted(glob.glob("extracted/indent_min_block*.csv"))

last_rows = []

for file in files:
    df = pd.read_csv(file)
    df_last = df.iloc[-1].copy()
    #print(f"\nFile: {os.path.basename(file)}")
    #print(df_last)
    df_last['filename'] = os.path.basename(file)

    last_rows.append(df_last)

combined = pd.DataFrame(last_rows)



dist = np.array([0, 13, 12.5, 12, 11.4, 11.2, 11.0])

combined['distance'] = dist
#print(combined)

#Doing curve of best fit

x = combined['distance'].iloc[1:]
y = combined['TotEng'].iloc[1:]

x = x.to_numpy()
y = y.to_numpy()

coefficients = np.polyfit(x, y, 2)
fit = np.poly1d(coefficients)

x_fit = np.linspace(min(x), max(x), 200)
y_fit = fit(x_fit)

plt.plot(x_fit, y_fit, color='Blue', label='Quadratic Fit', linestyle='--')
plt.scatter(combined['distance'].iloc[1:], combined['TotEng'].iloc[1:], label='LAMMPS data', color='Red')
plt.grid(alpha=0.5)
plt.xlabel('Indenter Distance')
plt.ylabel('Total Energy')
plt.title('Minimized Energy vs Indenter Distance')
plt.legend()
plt.savefig(f"plots/curated_plots/Indenter_Distance_Plot.png", dpi=150)
#plt.show()
