import math
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

# Set Params
tMin = 0
tMax = 2
Frequency = 10000 # of signal samples per t
ts = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax,1/Frequency)

# File Output Info
title = "RMS Values"
outputpng = "RMS_Graphically.png"
xlabel = "t"
ylabel = ""

# Functions
def f(t):
    return math.sin(2*math.pi*t)

def mean():
    mean = float(sum([(f(t)**2) for t in ts])) / max(len(ts), 1)
    return mean

rms = np.sqrt(mean())

def rmsval(t):
    return rms

# Plot data     "-","--","-.",":"
plt.plot(ts,[f(t) for t in ts], '-', linewidth=2, label="Function")
plt.plot(ts,[np.sqrt(f(t)**2) for t in ts], '--', linewidth=2, label="sqrt(Function^2)")
plt.plot(ts, [rmsval(t) for t in ts], '-.', linewidth=2, label="RMS: " + str(round(rms,3)))

# Plot settings
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.grid()
plt.legend()
plt.xlim(tMin, tMax)

# Save and Show Plot
plt.savefig(outputpng)
plt.show()
