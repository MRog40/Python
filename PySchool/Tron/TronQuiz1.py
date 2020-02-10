import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "Tron Quiz: $V_{ce}$ vs $I_b$"
unit1x, unit1y = 'A', 'V'
xlabel1 = "$I_b$"
ylabel1 = "$V_{ce}$"

title2 = "Tron Quiz: $V_{ce}$ vs $V_{be}$"
unit2x, unit2y = 'V', 'V'
xlabel2 = "$V_{be}$"
ylabel2 = "$V_{ce}$"

# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side
fig, (plt1, plt2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Plot Vce in terms of Ib
# Formatting
plt1.xaxis.set_major_formatter(EngFormatter(unit=unit1x))
plt1.yaxis.set_major_formatter(EngFormatter(unit=unit1y))
plt1.set_xticks(np.arange(0, 0.00022, 0.00005))

# Labels
plt1.set_title(title1)
plt1.set_xlabel(xlabel1)
plt1.set_ylabel(ylabel1)

# Function
def Vce1(I):
    return 20 - 100000*I

# Range of Ib
Ib = np.arange(0, 0.0002, 0.000001)
plt1.set_xlim(0, 0.00022)
plt1.set_ylim(0, 22)

# Plot
plt1.plot(Ib, [Vce1(I) for I in Ib])

# Now Plot Vce in terms of Vbe
# Formatting
plt2.xaxis.set_major_formatter(EngFormatter(unit=unit2x))
plt2.yaxis.set_major_formatter(EngFormatter(unit=unit2y))
plt2.set_xticks(np.arange(0, 0.76, 0.25))

# Labels
plt2.set_title(title2)
plt2.set_xlabel(xlabel2)
plt2.set_ylabel(ylabel2)

# Function
def Vce2(v):
    return 20 - 100000*np.exp(v/0.025)*10**(-16)

# Range of Vbe
Vbe = np.arange(0, 0.708104, 0.000001)
plt2.set_xlim(0, 0.75)
plt2.set_ylim(0, 22)

# Plot
plt2.plot(Vbe, [Vce2(v) for v in Vbe])

# Show the plots
plt.tight_layout()
plt.show()
