# LAMMPS Project Analysis

## LAMMPS Log Pipeline

### Parsing, Organizing and Plotting LAMMPS Simulations Output with Bash, awk and Python


This project analyzes builds a pipeline that turns raw LAMMPS log files into clean CSV files and plots, and runs with a single command (bash script).

THe simulation logs used in this project come from the sample set distributed with LAMMPS in a LAMMPS Github Repo. The Github repo is as following:


Additionally, The citation for LAMMPS is as follows:

Thompson, A. P., Aktulga, H. M., Berger, R., Bolintineanu, D. S., Brown, W. M., Crozier, P. S., et al. (2022). LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales. Comp. Phys. Comm., 271, 108171. DOI: 10.1016/j.cpc.2021.108171

To provide some background, LAMMPS is a molecular dynamics code, and every simulation writes a log file. A log file is not just a table of numbers. It contains the LAMMPS version and setup information, the input commands that were run, one or more thermo tables (Step, Temp, energies, pressure, and so on), and a timing and performance summary at the end. Moreover, the thermo columns are not the same from file to file, and they can even change inside a single file. For example, the minimization box log starts with the columns Step Temp Energy per pair, Energy per mol, Total Energy, Press and later switches to a different set of columns. Therefore, a parser that assumes fixed column positions breaks on real data.

The aim of this project is to build a parser that works from the structure of the file instead. Every thermo block starts at a line beginning with "Step" and ends at the line beginning with "Loop time of...". Each block is written to its own CSV file with its own header, and then the blocks are plotted. The project combines Linux command-line tools (bash,awk) for the file handling and extraction with Python (pandas, matplotlib) for the plotting.

## Project Structure and How to Run

```text
LAMMPS_Project/
├── raw/                               # original LAMMPS log files acquired from LAMMPS Github Repo
├── processed/                         # renamed copies of the logs
├── extracted/                         # one CSV per thermo block
├── plots/                             # generic plots (one per CSV)
│   └── curated_plots/                 # curated plots
├── scripts/                           # bash and Python scripts
├── block_labels.csv                   # description of every thermo block
├── run_pipeline.sh                    # runs the whole pipeline
└── README.md
```

Requirements are Linux or WSL with bash 4+ and awk. Python 3 with pandas and matplotlib and other imports are required too. To run the whole pipeline in bash:

git clone https://github.com/ashaheer1/LAMMPS_Project.git<br>
cd LAMMPS_Project<br>
./run_pipeline.sh<br>

The driver script clears the old outputs, rebuilds everything from raw/, and writes the CSV files to extracted/ and the plots to plots/. The block_labels.csv files is also copied to extracted/ to assist in labeling blocks and while plotting these blocks.


# The Input Data

For this project, I used four serial (1-processor) example logs from the LAMMPS examples of melt, min_box, indent, and indent_min. The trailing .1 in the original filenames is the number of MPI processors that were used for the run, and it is not a file format. I only used the .1 files. 

The simulation data analyzed in this project were generated using example LAMMPS simulations from the official LAMMPS repository:

- [Melt Example](https://github.com/lammps/lammps/tree/develop/examples/melt)
- [Minimization Example](https://github.com/lammps/lammps/tree/develop/examples/min)
- [Indentation Example](https://github.com/lammps/lammps/tree/develop/examples/indent)

Table 1 shows that each log contains.

<table align="center" border="1"> <tr> <th>Log</th> <th>Thermo Blocks</th> <th>What the Blocks Are</th> </tr> <tr> <td><code>melt</code></td> <td>1</td> <td>Simulation of Atomic Melt</td> </tr> <tr> <td><code>indent</code></td> <td>2</td> <td>Block 1 with the indenter, block 2 without the indenter</td> </tr> <tr> <td><code>indent_min</code></td> <td>7</td> <td>Initial minimization with indenter, then six diffeent indenter positions: y = 13.0, 12.5, 12.0, 11.4, 11.2, 11.0</td> </tr> <tr> <td><code>min_box</code></td> <td>8</td> <td>Block 1: melt<br> Block 2 minimize atoms only<br> Block 3 <code>box/relax iso</code> (Pxx = Pyy = 1.5)<br> Block 4 <code>box/relax aniso</code> (1.5)<br> Block 5 <code>box/relax x = 1.0 y = 2.0</code><br> Blocks 6 and 7 same as block 4 with tighter force tolerances<br> Block 8 <code>nreset 100</code> + even tighter force tolerance</td> </tr> </table> <div align="center">


# Results

Initially we created general plots for each block....

# Min Box Analysis

This is some of the results....

![Pressure Result](plots/melt_block1.png)
