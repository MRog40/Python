import numpy as np
import LTSpice_RawRead as LT
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import tkinter as tk; from tkinter import filedialog
 
# Get file to plot
tk.Tk().withdraw()
file_name = tk.filedialog.askopenfilename(initialdir = r"C:\Users\7258163\Documents\LTspiceXVII",title = "Select RAW File",filetypes = (("raw files","*.raw"),("all files","*.*")))

"""Traces are accessible by the method <LTSpiceReader instance>.get_trace(trace_ref) where trace_ref is either
the name of the net on the LTSPice Simulation. Normally trace references are stored with the format V(<node_name>)
for voltages or I(device_reference). For example V(n001) or I(R1) or Ib(Q1). """

def plotData(raw):
	x = raw.get_trace(0)
	for n in range(1, 30):
		try:
			plt.plot(x.data, raw.get_trace(n).data, label=raw.get_trace(n).name)
		except:
			return

raw = LT.LTSpiceRawRead(file_name)

plt.title("Test Plot")
plt.ylabel("Voltage")
plt.xlabel("Time")
#plt.xscale("log")
plt.yscale("linear")

plotData(raw)

plt.legend()
plt.grid(True)
plt.show()