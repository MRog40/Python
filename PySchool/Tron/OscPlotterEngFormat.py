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
title1 = askstring("Enter Plot Title", "Plot Title: ")
unit1x, unit1y = 's', 'V'
xlabel1 = "$Time$"
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
plt1.plot(Time,CH1, '-k', markersize=4, label="$V_{I}$")
plt1.plot(Time,CH2, ':k', markersize=4, label="$V_{O}$")

plt1.legend()
plt.tight_layout()
plt.show()
