import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "PreLab 5.2 MOSFET $V_{DS}$ DC Sweep"
unit1x, unit1y = 'V', 'A'
xlabel1 = "Voltage $V_{DS}$"
ylabel1 = "Current $I_D$"

# Figure
fig = plt.figure()
plt1 = fig.add_subplot(111)

# Formatting
plt1.xaxis.set_major_formatter(EngFormatter(unit=unit1x))
plt1.yaxis.set_major_formatter(EngFormatter(unit=unit1y))

# Labels
plt1.set_title(title1)
plt1.set_xlabel(xlabel1)
plt1.set_ylabel(ylabel1)

# Data
Vdsr = np.arange(0,10,0.01)

def Id(Vds, Vgs):
    chi = 0.001
    Vth = 1.5
    Vov = Vgs - Vth
    triode = chi*((Vgs - Vth) * Vds - 0.5 * Vds**2)
    saturation = 0.5*chi*(Vgs - Vth)**2
    if Vds > Vov:
        return saturation
    else:
        return triode

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
plt1.plot(Vdsr, [Id(V,3) for V in Vdsr], '-k', markersize=4, label="$V_{GS}: 3V$")
plt1.plot(Vdsr, [Id(V,5) for V in Vdsr], '--k', markersize=4, label="$V_{GS}: 5V$")

plt1.legend()
plt.tight_layout()
plt.show()
