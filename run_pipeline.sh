#!/bin/bash

set -e

cd "$(dirname "$0")"

echo "Starting it now"

echo "Start: [0/6] Cleaning Old Outputs..."
rm -f processed/*.log extracted/*_block*.csv plots/*.png plots/curated_plots/*.png
mkdir -p processed extracted plots plots/curated_plots

echo "[1/6] Organizing Raw Files..."
./scripts/organize.sh

echo "[2/6] Extracting Blocks From Organized Files..."
./scripts/extract.sh

echo "[3/6] Copying Labels File to Extraction Directory..."
cp block_labels.csv extracted/

echo "[4/6] Summarizing Extraction..."
./scripts/summarize.sh

echo "[5/6] Generating General Plots..."
python3 scripts/plots.py

echo "[6/6] Generating Curated Plots..."
python3 scripts/indent_min_plots.py
python3 scripts/indent_plots.py
python3 scripts/melt_plots.py
python3 scripts/min_box_convergence.py
python3 scripts/min_box_plots.py

echo "Pipeline Completed. Plots are in plots/"
