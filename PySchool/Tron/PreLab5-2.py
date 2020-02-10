import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "PreLab 5.4 MOSFET $R_{DS}$: $V_{GS}$ DC Sweep"
unit1x, unit1y = 'V', 'Ω'
xlabel1 = "Voltage $V_{GS}$"
ylabel1 = "Resistance $R_{DS}$"

xscale = 'linear'
yscale = 'log'

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

# Data
Vgsr = np.arange(0.01,10,0.01)

def Id(Vds, Vgs):
    chi = 0.001
    Vth = 0
    return chi*((Vgs - Vth) * Vds - 0.5 * Vds**2)

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
plt1.plot(Vgsr, [0.000001/Id(0.000001,V) for V in Vgsr], '-k', markersize=4, label="$R_{DS}$")

plt1.legend()

plt.grid(which='both')
plt.tight_layout()
plt.show()
