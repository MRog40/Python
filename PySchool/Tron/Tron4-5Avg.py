import math
import pandas as pd
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

# Heaviside Function
def u(t):
    return 0 if t < 0 else 1
# Ramp Function
def r(t):
    return 0 if t < 0 else t
# Impulse Function (kind of)
def dirac(t):
    return float('inf') if t==1 else 0

# Set Params
tMin = 0
tMax = math.pi*4
Frequency = 1000 # of signal samples per t
ts = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax,1/Frequency)

# File Output Info
title = "Tron 4.5"
outputpng = "Tron4-5.png"
xlabel = "t"
ylabel = ""

# Functions
def f1(t):
    return 6*0.9*math.sin(t)
def f2(t):
    return 6 if 6*0.9*math.sin(t) > 3 else 0

# Plot data     "-","--","-.",":"
plt.plot(ts,[f1(t) for t in ts], '-', linewidth=1, label="Vi")
plt.plot(ts,[f2(t) for t in ts], '--', linewidth=1, label="Ib avg: "+str(np.mean([f2(t) for t in ts])))

# Plot settings
#plt.semilogt()
#plt.semilogy()
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend()
plt.xlim(tMin, tMax)

# Save and Show Plot
plt.savefig(outputpng)
plt.show()
