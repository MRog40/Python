import numpy as np
import math
import matplotlib.pyplot as plt

# Circuit Parameters
Zg = 8 + 8j
Zl = 8 + 16j
Z = Zg + Zl
Vphasor = 60*np.exp(1j*np.deg2rad(0))
Iphasor = Vphasor / Z

# Graph Parameters
tMin = 0
tMax = 2/60
s_freq = 100000

def Vg(t):
    return 60*np.sin(2*np.pi*60*t)

def I(t):
    phi = np.angle(Iphasor)
    return Vg(t + phi)/Z

def Vl(t):
    return Vg(t)*(Zl/Z)

def Pow(t):
    return I(t)*Vg(t)

def PowFactor():
    S = Iphasor**2*Z
    P = Iphasor**2*(Z.real)
    return abs(P/S)

ts = np.arange(tMin, tMax, 1/s_freq)

# Plot data
plt.plot(ts, [Vg(t) for t in ts], label="V Gen (V)", linewidth = 1)
plt.plot(ts, [Vl(t) for t in ts], label="V Load (V)", linewidth = 1)
plt.plot(ts, [10*I(t) for t in ts], label="I*10 (A)", linewidth = 1)
plt.plot(ts, [Pow(t)/10 for t in ts], label="Power/10 (W)", linewidth = 1)

# Plot settings
plt.title("Zg: " + str(Zg) + ", Zl: " + str(Zl) + ", PF = " + str(round(PowFactor(), 4)))
plt.xlabel("Time (s)")
plt.legend()
plt.grid()

plt.show()
