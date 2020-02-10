import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "Lab 5 PMOS FET I-V Characteristic"
unit1x, unit1y = 'V', 'A'
xlabel1 = "Voltage $V_{SD}$"
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
#plt1.set_xlim(-0.0001,0.0011)

# Data
Vsd3 = [	0,	0.25,	0.5,	1,	1.25,	1.5,	1.75,	2,	2.5,	3,	4,	5,	6,	7,	8,	9,	10]
Id3m = [	0.003,	0.2,	0.346,	0.511,	0.552,	0.566,	0.591,	0.595,	0.619,	0.641,	0.685,	0.719,	0.75,	0.78,	0.795,	0.812,	0.832]
																		
Vsd5 = [	0,	0.5,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	8,	9,	10]
Id5m = [	0.0139,	0.864,	1.568,	2.153,	2.588,	2.893,	3.086,	3.218,	3.315,	3.399,	3.475,	3.543,	3.608,	3.6669,	3.728,	3.769,	3.802,	3.834]

Id3 = [i/1000 for i in Id3m]
Id5 = [i/1000 for i in Id5m]

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
plt1.plot(Vsd5, Id5, '--ok', markersize=4, label="$V_{SG}: 5V$")
plt1.plot(Vsd3, Id3, '-ok', markersize=4, label="$V_{SG} 3V$")

plt1.legend()
plt.tight_layout()
plt.show()
