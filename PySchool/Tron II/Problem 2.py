import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "Problem 2: Sources"
unit1x, unit1y = 'mA', 'V'
xlabel1 = "Current"
ylabel1 = "Voltage"

xscale = 'linear'
yscale = 'linear'

# Figure
fig = plt.figure()
plt1 = fig.add_subplot(111)
plt1.set_yscale(yscale)
plt1.set_xscale(xscale)

# Formatting
plt1.xaxis.set_major_formatter(EngFormatter(unit=unit1x))
plt1.yaxis.set_major_formatter(EngFormatter(unit=unit1y))

# Labels
plt1.set_title(title1)
plt1.set_xlabel(xlabel1)
plt1.set_ylabel(ylabel1)
#plt1.set_xlim(-0.0001,0.0011)

# Data
voltage = [13.213,	12.585,	12.464,	12.417,	12.369 ]
current = [0,	24.6764705882353,	48.878431372549,	73.0411764705882,	97.0117647058824]

# Plot
plt1.plot(current, voltage, '-ok', markersize=4)

#plt.grid(which='both')
plt.legend()
plt.tight_layout()
plt.show()