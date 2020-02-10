import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "Lab 5 NMOS FET Varying Rail Voltage"
unit1x, unit1y = 'V', 'V'
xlabel1 = "Voltage $V_{S}$"
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
Vs = [0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20]
Vo = [	0,	0.186,	0.387,	0.605,	0.843,	1.112,	1.429,	1.827,	2.403,	3.216,	4.137,	5.09,	6.056,	7.028,	8.002,	9.023,	9.985,	10.967,	11.951,	12.932,	13.92]

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

def iVo(Vs):
    return Vs*250/(986+250)

Vs1 = np.arange(0,20,0.1)

# Plot
plt1.plot(Vs, Vo, '-ok', markersize=4, label='$V_O$ Exp')
plt.plot(Vs1, [iVo(x) for x in Vs1], '--k', label='$V_O$ Ideal')

#plt.grid(which='both')
plt.legend()
plt.tight_layout()
plt.show()