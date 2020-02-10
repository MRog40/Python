import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "Lab 3 PNP Junctions: $Resistance$ vs $Current$"
unit1x, unit1y = 'A', 'Ω'
xlabel1 = "$Current$"
ylabel1 = "$Resistance$"

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
plt1.set_xlim(0.00000008,0.0011)
plt1.loglog()

# Data
I =	[0.0000001,	0.000001,	0.0001,	0.001]
Rbc	= [3583000,	434400,	5787,	664.5]
Rbe	= [4059000,	469800,	5970,	673]

Rcb = [4097000,	478600,	6193,	694.8]
Reb	= [4218000, 486400,	6225,	697.3]


# Plot
plt1.plot(I,Rcb, '-ok', markersize=4,  label="$R_{CB}$")
plt1.plot(I,Reb,'--+k', markersize=8,  label="$R_{EB}$")

plt1.legend()
plt.tight_layout()
plt.show()
