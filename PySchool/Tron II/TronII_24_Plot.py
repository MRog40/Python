import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

# Plot Data
OGtitle = "Power Amplifier Efficiency vs Power Out"
xlabel = "Power (W)"
ylabel = "Efficiency"

# Experimental Data
voltages = [5, 10, 15, 20, 25, 30, 32, 34, 36]
currents = [0.0288, 0.0581, 0.0889, 0.1240, 0.1660, 0.2200, 0.2415, 0.2721, 0.3184]
Po = [13.077*(c-0.002) for c in currents]
P = [v**2/(8*50) for v in voltages]
Pd = [Po1-P1 for P1, Po1 in zip(P,Po)]

efficiency = [P1/Po1 for P1, Po1 in zip(P,Po)]

# print("\nEfficiency")
# for eff in efficiency:
#     print(str(round(eff*100, 1)) + " %")

# print("\nPower Dissipated")
# for p in Pd:
#     print(str(round(p*1000, 1)) + " mW")

# Plot data
plt.plot(P, efficiency)

# Plot settings
#plt.semilogx()
#plt.semilogy()
#plt.grid()
plt.title(OGtitle)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
#plt.legend()

# Save and Show Plot
plt.show()

plt.plot(P, Pd)
plt.title("Power Dissipated vs Power Out")
plt.xlabel(xlabel)
plt.ylabel("Power Dissipated")
plt.show()
