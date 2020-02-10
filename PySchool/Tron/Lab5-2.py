import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "Lab 5 NMOS FET Variable Conductor"
unit1x, unit1y = 'V', 'S'
xlabel1 = "Voltage $V_{GS}$"
ylabel1 = "Conductance   $G_{DS}$"

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
Vgs = [	0.5,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	8,	9,	10]
Rds =	[8343000,	65500,	1530,	745,	491,	476.3,	365.1,	309.6,	274.6,	250,	231.4,	216.9,	205,	195.1,	179.7,	168.1,	158.9]

Gds = [1/i for i in Rds]

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
plt1.plot(Vgs, Gds, '-ok', markersize=4)

#plt.grid(which='both')
plt.tight_layout()
plt.show()
