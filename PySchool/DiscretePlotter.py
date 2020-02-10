import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

# Plot Data
title = "Output Audio Voltage vs Input Voltage"
xlabel = "Input Voltage (mV)"
ylabel = "Output Audio Voltage (mV)"

# Experimental Data
Vin = [0.5, 	1, 	2, 	4, 	6, 	8, 	10, 	12, 	14, 	16, 	18, 	20, 	22, 	24, 	26, 	28, 	30, 	32, 	35]
Vout = [92, 	140, 	183, 	217, 	250, 	294, 	350, 	410, 	469, 	510, 	540, 	569, 	584, 	596, 	604, 	610, 	616, 	622, 	628]

# Fit equation
# m,b = np.polyfit(Vin, Vout, 1)
# fit_eqn = "y = " + str(round(m,4)) + "x + " + str(round(b,4))

# Po = [13.077*(c-0.002) for c in currents]
# P = [v**2/(8*50) for v in voltages]
# Pd = [Po1-P1 for P1, Po1 in zip(P,Po)]

# efficiency = [P1/Po1 for P1, Po1 in zip(P,Po)]

# Plot data
plt.plot(Vin, Vout, 'o-k', markersize=2)

# Plot settings
plt.semilogx()
plt.semilogy()
#plt.grid()
#plt.legend([fit_eqn])
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
#plt.legend()

plt.show()