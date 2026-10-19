import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os
import re

labels = pd.read_csv("extracted/block_labels.csv")

def get_label(name):
    m = re.match(r"(.+)_block(\d+)$", name)
    if not m:
        return name
    f, b = m.group(1), int(m.group(2))
    row = labels[(labels.file == f) & (labels.block == b)]
    return row.description.iloc[0] if not row.empty else name

files = glob.glob("extracted/*.csv")

os.makedirs("plots", exist_ok=True)

for file in files:
    if os.path.basename(file) == 'block_labels.csv':
        continue
    df = pd.read_csv(file)
    name = os.path.splitext(os.path.basename(file))[0]
    #cols = [c for c in df.columns if c.lower() != 'step']
    cols= []
    for c in df.columns:
        if c.lower() != 'Step':
            cols.append(c)
    fig, axes = plt.subplots(len(cols), 1, figsize=(8, 2.5 * len(cols)), sharex=True)
    if len(cols) == 1:
        axes = [axes]
    for ax, col in zip(axes, cols):
        ax.plot(df['Step'], df[col], lw=0.8)
        ax.set_ylabel(col)
        ax.grid(alpha=0.3)
    axes[-1].set_xlabel('Step')
    fig.suptitle(get_label(name), y=0.98)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(f"plots/{name}.png", dpi=150)
    plt.close(fig)
