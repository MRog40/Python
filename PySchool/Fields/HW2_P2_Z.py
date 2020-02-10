import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk; from tkinter import filedialog
from tkinter.simpledialog import askstring, askinteger

# Load tkinter
tk.Tk().withdraw()

# Rad, m, Ohms, Ohms
B = 3.6 
l = 0.05
Zo = 80
Zl = 75+45j

# Plot Data
title = "Zin(z)" #askstring("Enter Plot Title", "Plot Title: ")
xlabel = "Z on Line (m)"
ylabel = "Magnitude of Impedance (Ohms)"

def Zin(z, B, l, Zo, Zl):
    Numer = Zl-1j*Zo*np.tan(np.degrees(B*(l-z)))
    Denom = Zo-1j*Zl*np.tan(np.degrees(B*(l-z)))
    return Zo*(Numer/Denom)

Line = np.arange(0, l, 0.00005)

# Plot data
plt.plot(Line, [Zin(z, B, l, Zo, Zl).real for z in Line], label="Re{Zin}")
plt.plot(Line, [Zin(z, B, l, Zo, Zl).imag for z in Line],label="Im{Zin}")
plt.plot(Line, [abs(Zin(z, B, l, Zo, Zl)) for z in Line], 'r', label="|Zin|")

# Plot settings
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend()

# Get user input of where to save file
#save_path = tk.filedialog.asksaveasfilename(initialfile = title + ".png",
#                                            title = "Save Plot As", defaultextension='.png',
#                                            filetypes=[('PNG file','*.png')])

# Save and Show Plot
#plt.savefig(save_path)
plt.show()