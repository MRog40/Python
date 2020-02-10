import matplotlib.pyplot as plt
import numpy as np
# Calculate and plot the velocity 
# of a linear motor as a function of load
VB = 120                # Battery Voltage (V)
r = 0.3                 # Resistance (Ohms)
l = 1                   # Bar length (m)
B = 0.6                 # Flux density (T)
# Range of forces on the bar (From, to, step)
F = np.arange(0, 51, 10)
# Currents
i = F / (l * B)
# Voltages
eind = VB - i * r
# Velocities
V_bar = eind / (l * B)
# Plot
plt.plot(F, V_bar)
plt.title('Plot of Velocity versus Applied Force')
plt.xlabel('Force (N)')
plt.ylabel('Velocity (m/s)')
plt.axis([0, 50, 0, 200])
plt.show()