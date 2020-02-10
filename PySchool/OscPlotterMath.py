import pandas
import csv
import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import tkinter as tk; from tkinter import filedialog
from tkinter.simpledialog import askstring, askinteger
from scipy.interpolate import BSpline

# Get CSV path with gui
tk.Tk().withdraw()
file_path = tk.filedialog.askopenfilename()

# Plot Data
title = askstring("Enter Plot Title", "Plot Title: ")
xlabel = "Voltage (V)"
ylabel = "Voltage (V)"

# Read Files and store
colnames = ['X', 'CH1', 'CH2']
data = pandas.read_csv(file_path, skiprows = 2)

Time = data.iloc[:,0]
CH1 = data.iloc[:,1]
CH2 = data.iloc[:,2]

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

def current(List1, R):
    curr = [List1[0] / R]
    iterList1 = iter(List1)
    next(iterList1)
    for x in iterList1:
        curr.append(x/R)
    return curr

x = CH2
y = current(CH1, 197.4)

# Plot data
#plt.scatter(x, y, s=3, label="Id (A)")

# Find and do a trendline
srtd = sorted(zip(x, y), key=lambda x: x[0])
x, y = zip(*srtd)
plt.plot(x, y, 'b', linewidth=1)

# Plot settings
#plt.semilogx()
#plt.semilogy()
plt.grid()
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Get user input of where to save file
#save_path = tk.filedialog.asksaveasfilename(initialfile = title + ".png",
#                                            title = "Save Plot As", defaultextension='.png',
#                                            filetypes=[('PNG file','*.png')])

# Save and Show Plot
#plt.savefig(save_path)
plt.show()