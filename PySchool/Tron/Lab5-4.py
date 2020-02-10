import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "Lab 5 CMOS Digital Inverter Sweep"
unit1x, unit1y = 'V', 'V'
xlabel1 = "Voltage $V_{I}$"
ylabel1 = "Voltage $V_{O}$"

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
vi = [	0,	0.5,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5]
vo = [	5,	5,	5,	4.931,	4.383,	0.135,	0.01,	0,	0,	0,	0]

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
plt1.plot(vi, vo, '-ok', markersize=4)

#plt.grid(which='both')
plt.legend()
plt.tight_layout()
plt.show()