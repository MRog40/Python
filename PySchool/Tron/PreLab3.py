import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Global settings
title1 = "PreLab 3 Part 4: $V_{ec}$ vs $V_{1}$"
unit1x, unit1y = 'V', 'V'
xlabel1 = "$Voltage$"
ylabel1 = "$Voltage$"

title2 = "PreLab 3 Part 4: $V_{cb}$ vs $V_{1}$"
unit2x, unit2y = 'V', 'V'
xlabel2 = "$Voltage$"
ylabel2 = "$Voltage$"

# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side
fig, (plt1, plt2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Plot Vce in terms of Ib
# Formatting
plt1.xaxis.set_major_formatter(EngFormatter(unit=unit1x))
plt1.yaxis.set_major_formatter(EngFormatter(unit=unit1y))
# plt1.set_xticks(np.arange(0, 0.00022, 0.00005))

# Labels
plt1.set_title(title1)
plt1.set_xlabel(xlabel1)
plt1.set_ylabel(ylabel1)

# Function
def Vce1(I):
    Vce = (9.3-I)/2
    if Vce > 10:
        Vce = 10
    return Vce

# Range of Ib
Ib = np.arange(0, 12, 0.001)
plt1.set_xlim(0, 12)
plt1.set_ylim(-1, 11)

# Plot
plt1.plot(Ib, [Vce1(I) for I in Ib])

# Now Plot Vce in terms of Vbe
# Formatting
plt2.xaxis.set_major_formatter(EngFormatter(unit=unit2x))
plt2.yaxis.set_major_formatter(EngFormatter(unit=unit2y))
# plt2.set_xticks(np.arange(0, 0.76, 0.25))

# Labels
plt2.set_title(title2)
plt2.set_xlabel(xlabel2)
plt2.set_ylabel(ylabel2)

# Function
def Vce2(v):
    return 0.7 - Vce1(v)

# Range of Vbe
Vbe = np.arange(0, 12, 0.01)
plt2.set_xlim(0, 12)
plt2.set_ylim(-1, 11)

# Plot
plt2.plot(Vbe, [Vce2(v) for v in Vbe])

# Show the plots
plt.tight_layout()
plt.show()
