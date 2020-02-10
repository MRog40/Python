import matplotlib.pyplot as plt
import numpy as np

tMin = 0
tMax = 0.02
sample_rate = 1000000

Is = 10**(-9)
n = 1.75
Vt = 25*10**(-3)
V_Diode = 0.7

ts = np.arange(0, 5, 1/sample_rate)

def I(v):
    return Is*(np.exp(v/(n*Vt))-1)

def Diode(x):
    return 0 if x < V_Diode else x - V_Diode

# Plot data
# plt.plot(Vd, [I(v) for v in Vd], 'black')
plt.plot(ts, [Diode(10*np.sin(2*np.pi*100*t)) for t in ts], 'black')

# Plot settings
#plt.semilogx()
# plt.semilogy()
#plt.grid()
plt.title("PreLab #4")
plt.xlabel("Time (s)")
plt.ylabel("V")
plt.xlim(tMin, tMax)

# Save and Show Plot
plt.savefig("Tron_PL1-4.png")
plt.show()
