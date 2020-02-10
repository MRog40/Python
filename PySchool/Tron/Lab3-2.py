import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import tkinter as tk; from tkinter import filedialog
from tkinter.simpledialog import askstring, askinteger

# Get CSV path with gui
tk.Tk().withdraw()
file_path = tk.filedialog.askopenfilename()

# Read File and store
colnames = ['X', 'CH1', 'CH2']
data = pandas.read_csv(file_path, skiprows = 2)

Time = data.iloc[:,0]
CH1 = data.iloc[:,1]
CH2 = data.iloc[:,2]

# Global settings
title1 = "Lab 3 NPN BJT Inverter: $Simulation$ vs $Experiment$"
unit1x, unit1y = 'V', 'V'
xlabel1 = "$Voltage$"
ylabel1 = "$Voltage$"

# Figure
fig = plt.figure()
plt1 = fig.add_subplot(111)

# Formatting
plt1.xaxis.set_major_formatter(EngFormatter(unit=unit1x))
plt1.yaxis.set_major_formatter(EngFormatter(unit=unit1y))

# Labels
plt1.set_title(title1)
plt1.set_xlabel(xlabel1)
plt1.set_ylabel(ylabel1)
#plt1.set_xlim(-0.0001,0.0011)

# Data
V1 = [0,    0.5 ,   1,  1.5,    2,	3,	4,	5,	5.5,	6,	6.5,	7,	7.5,	8,	9,	10,	11,	12]
Vc = [9.997,	9.989,	9.496,	8.795,	8.048,	6.54,	5.007,	3.488,	2.71,	2.017,	1.295,	0.557,	0.237,	0.202,	0.175,	0.162,	0.152,	0.144]
Vb = [-0.006,	0.481,	0.611,	0.632,	0.643,	0.657,	0.666,	0.673,	0.676,	0.68,	0.683,	0.684,	0.687,	0.688,	0.686,	0.686,	0.686,	0.686]
Ve = [-0.005,	-0.005,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006,	-0.006]

# Calculate Diff List1 - List2
def diff(List1, List2):
    diff = [List1[0] - List2[0]]
    iterList1 = iter(List1)
    iterList2 = iter(List2)
    next(iterList1)
    next(iterList2)
    for x, y in zip(iterList1, iterList2):
        diff.append(x-y)
    return diff
    
# Plot
plt1.plot(V1,diff(Vb,Vc), '-ok', markersize=4, label="$V_{BC} Exp$")
plt1.plot(V1,diff(Vc,Ve), '--ok', markersize=4, label="$V_{CE} Exp$")
plt1.plot(Time,CH2, '-k', markersize=4, label="$V_{BC} Sim$")
plt1.plot(Time,CH1, '--k', markersize=4, label="$V_{CE} Sim$")

plt1.legend()
plt.tight_layout()
plt.show()
