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
title1 = "Lab 3 PNP DC Sweep: $Input$ Voltage"
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
V1 = [0, 1,	2,	3,	4,	5,	6,	7,	8,	8.5,	9,	9.5,	10,	10.5,	11,	12]
Vc = [-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01]
Vb = [3.64,	4.228,	4.824,	5.423,	6.027,	6.633,	7.245,	7.857,	8.474,	8.784,	9.097,	9.422,	9.891,	10.386,	10.88,	11.871]
Ve = [4.342,	4.921,	5.517,	6.116,	6.72,	7.324,	7.934,	8.541,	9.151,	9.452,	9.749,	10, 10.008,	10.008,	10.008,	10.008]

V1wide = [-12,	-11,	-10,	-9,	-8.5,	-8,	-7.5,	-7,	-6,	-4,	-2,	0, 1,	2,	3,	4,	5,	6,	7,	8,	8.5,	9,	9.5,	10,	10.5,	11,	12]
Vewide = [0.097,	0.105,	0.117,	0.133,	0.146,	0.166,	0.217,	0.365,	0.895,	2.002,	3.166,	4.342,	4.921,	5.517,	6.116,	6.72,	7.324,	7.934,	8.541,	9.151,	9.452,	9.749,	10, 10.008,	10.008,	10.008,	10.008]
Vcwide = [-0.01,-0.01,-0.01,-0.01,-0.01,-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01,	-0.01, -0.01,	-0.01,	-0.01, -0.01,	-0.01,	-0.01,	-0.01]

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
plt1.plot(V1, diff(Ve,Vc), '-ok', markersize=4, label="$V_{EC} Exp$")
plt1.plot(V1, diff(Vb,Vc), '--ok', markersize=4, label="$V_{BC} Exp$")
plt1.plot(Time,CH1, '-k', markersize=4, label="$V_{EC} Sim$")
plt1.plot(Time,CH2, '--k', markersize=4, label="$V_{BC} Sim$")

plt1.legend()
plt.tight_layout()
plt.show()
