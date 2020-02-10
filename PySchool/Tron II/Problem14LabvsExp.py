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
OGtitle = "Cohn Filter Exp vs Simulation"
xlabel = "Frequency (Hz)"
ylabel = "Relative Loss (dB)"

# Read Files and store
colnames = ['freq', 'dB']
data = pandas.read_csv(file_path, skiprows = 1)

freq = data.iloc[:,0]
dB = data.iloc[:,1]

# Experimental Data
freq_exp = [4912350, 	4912400, 	4912450, 	4912500, 	4912550, 	4912600, 	4912650, 	4912700, 	4912750, 	4912800, 	4912850, 	4912900, 	4912950, 	4913000, 	4913050, 	4913100, 	4913150, 	4913200, 	4913250, 	4913300, 	4913350, 	4913400, 	4913450, 	4913500, 	4913550, 	4913600, 	4913650, 	4913700, 	4913750, 	4913800, 	4913850, 	4913900, 	4913950, 	4914000, 	4914050, 	4914100, 	4914150, 	4914200, 	4914250, 	4914300, 	4914350, 	4914400, 	4914450, 	4914500, 	4914550, 	4914600, 	4914650, 	4914700, 	4914750, 	4914800, 	4914850 ]
dB_exp = [-57.73920973, 	-57.04396761, 	-56.40027394, 	-56.09547461, 	-55.51620069, 	-54.97315577, 	-53.97940009, 	-53.30223474, 	-52.47438104, 	-51.0233677, 	-49.63683787, 	-48.44147377, 	-46.55304952, 	-44.83731726, 	-42.899117, 	-40.73445614, 	-38.10887785, 	-35.48124737, 	-32.25509027, 	-28.87069013, 	-24.8270805, 	-20.23798447, 	-14.71385623, 	-8.45699815, 	-3.293045401, 	-2.989724544, 	-3.031224335, 	-3.031224335, 	-3.006300674, 	-3.006300674, 	-2.998008655, 	-3.006300674, 	-3.064567522, 	-9.708327075, 	-16.28471716, 	-22.11607452, 	-26.9488014, 	-31.21334612, 	-34.97315577, 	-38.29978421, 	-41.82160939, 	-44.43697499, 	-46.75505605, 	-48.69325631, 	-50.53618078, 	-51.71860982, 	-53.52214243, 	-54.46207368, 	-55.80100947, 	-56.71615928, 	-57.38463439]

# Plot data
plt.plot(freq, dB, label = "Simulation")
plt.plot(freq_exp, dB_exp, label = "Experimental")

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