import pandas
import csv
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk; from tkinter import filedialog
from tkinter.simpledialog import askstring, askinteger

plt.rcParams["font.family"] = "Times New Roman"

# Get CSV path with gui
tk.Tk().withdraw()
file_path = tk.filedialog.askopenfilename()

# Plot Data
OGtitle = askstring("Enter Plot Title", "Plot Title: ")
xlabel = "Time (s)"
ylabel = "AC Voltage (V)"

# Read Files and store
colnames = ['X', 'CH1', 'CH2']
data = pandas.read_csv(file_path, skiprows = 2)

Time = data.iloc[:,0]
CH1 = data.iloc[:,1]
CH2 = data.iloc[:,2]

def offset(List1, off):
    diff = [List1[0] - off]
    iterList1 = iter(List1)
    next(iterList1)
    for x in iterList1:
        diff.append(x-off)
    return diff

def findoff(ch):
    return (max(ch) + min(ch))/2

shift1 = round(findoff(CH1),4)
shift2 = round(findoff(CH2),4)

labelCH1 = label="$V_{IN}$ - " + str(shift1) + " $V_{DC}$"
labelCH2 = label="$V_{OUT}$ - " + str(shift2) + " $V_{DC}$"

# Plot data
plt.plot(Time, offset(CH1, shift1),'-k', markersize=4, label = labelCH1)
#plt.plot(Time, offset(CH2, shift2),'--k', markersize=4, label = labelCH2)
#plt.plot(Time, diff(CH1, CH2), "CH1 - CH2 (V)")

# Plot settings
#plt.semilogx()
#plt.semilogy()
#plt.grid()
plt.title(OGtitle)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend()

# Get user input of where to save file
save_path = tk.filedialog.asksaveasfilename(initialfile = OGtitle + ".png",
                                            title = "Save Plot As", defaultextension='.png',
                                            filetypes=[('PNG file','*.png')])

# Save and Show Plot
plt.savefig(save_path)
plt.show()