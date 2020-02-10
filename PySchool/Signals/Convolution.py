import math
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

# Set Params
tMin = -5
tMax = 5
freq = 5000 # of signal samples per t
ts = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax, 1/freq)

# Heaviside Function
def u(t):
    return 0 if t < 0 else 1
# Ramp Function
def r(t):
    return 0 if t < 0 else t
# Rectangle Function
def rect(t):
    return 1 if -1/2 < t < 1/2 else 0
# Impulse Function
def dirac(t):
    return float('inf') if t==1 else 0

# Functions
def x(t):
    return 1.1 * rect((t-2)/5)
def h(t):
    return 1.5 * rect((t-1)/3)

# Convolve the functions
xa = ts[:]
ha = ts[:]
for i, t in enumerate(ts):
    xa[i] = x(t)
    ha[i] = h(t)
ya = np.convolve(xa, ha)

# Convolution time range of two signals with lengths M, N is: M + N - 1
ts_convolved = np.arange(tMin-tMax, tMax - tMin + 2 if isinstance(tMax, int) else tMax - tMin, 1/freq)
ts_convolved = ts_convolved[:-1]

print("len(ts): " + str(len(ts)))
print("len(ya): " + str(len(ts)))
print("len(ts_con): " + str(len(ts_convolved)))

# Plot data
plt.plot(ts, xa, label="x(t)")
plt.plot(ts, ha, label="h(t)")
plt.plot(ts_convolved, ya, label="x(t) convolve h(t)")

# Plot settings
plt.title("Convolved Signals")
plt.xlabel('t (s)')
plt.legend()
plt.grid(linestyle=':')

plt.show()