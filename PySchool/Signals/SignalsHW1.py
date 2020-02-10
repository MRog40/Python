import math
import pandas as pd
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

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

# Set Params
tMin = -4
tMax = 4
discrete_time_frequency = 1000 # of signal samples per t
discrete_times = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax,1/discrete_time_frequency)

# Plot data
plt.plot(discrete_times,[5*r(t+2)-5*r(t)-10*u(t) for t in discrete_times], '-', label="1.22 (b): x2(t)")
plt.plot(discrete_times,[10*rect((t+1)/2)-10*rect((t-3)/2) for t in discrete_times], '--', label="1.22 (d): x4(t)")

# Plot settings
plt.title("Signals HW1 Problem 1.22 Michael Rogers")
plt.xlabel('t (s)')
plt.legend()
plt.xlim(tMin, tMax)
plt.grid(linestyle=':')

# Save and Show Plot
plt.savefig("Signals_1-22.png")
plt.show()
plt.clf()

#P2###################################################################################################
tMin = -10
tMax = 10
discrete_time_frequency = 1000 # of signal samples per t
discrete_times = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax,1/discrete_time_frequency)

# Function
def x(t):
    return 0 if t <= 2 else 2*t-4

# Plot data
plt.plot(discrete_times,[x(t) for t in discrete_times], '-', label="1.8: x(t)")
plt.plot(discrete_times,[x(t+1) for t in discrete_times], '--', label="1.8: x(t+1)")
plt.plot(discrete_times,[x((t+1)/2) for t in discrete_times], '-,', label="1.8: x((t+1)/2)")
plt.plot(discrete_times,[x(-(t+1)/2) for t in discrete_times], ':', label="1.8: x(-(t+1)/2)")

# Plot settings
plt.title("Signals HW1 Problem 1.8 Michael Rogers")
plt.xlabel('t (s)')
plt.legend()
plt.xlim(tMin, tMax)
plt.grid(linestyle=':')

# Save and Show Plot
plt.savefig("Signals_1-8.png")
plt.show()
plt.clf()

#P3###################################################################################################
tMin = -8
tMax = 8
discrete_time_frequency = 1000 # of signal samples per t
discrete_times = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax,1/discrete_time_frequency)

# Function
def x(t):
    return 0 if t < 2 else 0 if t > 6 else r(t-2)

# Plot data
plt.plot(discrete_times,[x(t) for t in discrete_times], '-', label="1.11: x(t)")
plt.plot(discrete_times,[x(2*t+6) for t in discrete_times], '--', label="1.11(a): x(2*t+6)")
plt.plot(discrete_times,[x(-2*t+6) for t in discrete_times], '-,', label="1.11(b): x(-2*t+6)")
plt.plot(discrete_times,[x(-2*t-6) for t in discrete_times], ':', label="1.11(c): x(-2*t-6)")

# Plot settings
plt.title("Signals HW1 Problem 1.11 Michael Rogers")
plt.xlabel('t (s)')
plt.legend()
plt.xlim(tMin, tMax)
plt.grid(linestyle=':')

# Save and Show Plot
plt.savefig("Signals_1-11.png")
plt.show()
plt.clf()

#P4###################################################################################################
tMin = -10
tMax = 10
discrete_time_frequency = 1000 # of signal samples per t
discrete_times = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax,1/discrete_time_frequency)

# Functions
def x1(t):
    return 3*t**2 + 4*t**4
def x2(t):
    return 3*t**3

# Plot data
plt.plot(discrete_times,[x1(t) for t in discrete_times], '-', label="1.16(a): x1(t) is Even")
plt.plot(discrete_times,[x2(t) for t in discrete_times], '--', label="1.16(b): x2(t) is Odd")

# Plot settings
plt.title("Signals HW1 Problem 1.16 Michael Rogers")
plt.xlabel('t (s)')
plt.legend()
plt.xlim(tMin, tMax)
plt.grid(linestyle=':')

# Save and Show Plot
plt.savefig("Signals_1-16.png")
plt.show()
plt.clf()

#P5###################################################################################################
tMin = -2
tMax = 4
discrete_time_frequency = 1000 # of signal samples per t
discrete_times = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax,1/discrete_time_frequency)

# Plot data
plt.plot(discrete_times,[4*u(t+1) for t in discrete_times], '-', label="1.21(a): 4*u(t+1)")
plt.plot(discrete_times,[-2*u(t+2)+2*u(t-2) for t in discrete_times], '--', label="1.21(b): -2*u(t+2)+2*u(t-2)")
plt.plot(discrete_times,[2*u(t)+2*u(t-2)+2*u(t-3) for t in discrete_times], '-,', label="1.21(c): 2*u(t)+2*u(t-2)+2*u(t-3)")
plt.plot(discrete_times,[6*u(t)-2*u(t-1)-2*u(t-3)-2*u(t-4) for t in discrete_times], ':', label="1.21(d): 6*u(t)-2*u(t-1)-2*u(t-3)-2*u(t-4)")
plt.plot(discrete_times,[2*u(t)+4*u(t-1)-4*u(t-3)-2*u(t-4) for t in discrete_times], '-', label="1.21(e): 2*u(t)+4*u(t-1)-4*u(t-3)-2*u(t-4)")
plt.plot(discrete_times,[4*u(t)-6*u(t-1)+6*u(t-2)-4*u(t-3) for t in discrete_times], '-', label="1.21(f): 4*u(t)-6*u(t-1)+6*u(t-2)-4*u(t-3)")

# Plot settings
plt.title("Signals HW1 Problem 1.21 Michael Rogers")
plt.xlabel('t (s)')
plt.legend()
plt.xlim(tMin, tMax)
plt.grid(linestyle=':')

# Save and Show Plot
plt.savefig("Signals_1-21.png")
plt.show()
plt.clf()

#P6###################################################################################################
tMin = 0
tMax = 2*np.pi
discrete_time_frequency = 1000 # of signal samples per t
discrete_times = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax,1/discrete_time_frequency)

# Plot data
plt.plot(discrete_times,[math.sin(2*t) for t in discrete_times], '-', label="1.26(a): sin(2t) Period T=pi")
plt.plot(discrete_times,[math.cos(np.pi/3*t) for t in discrete_times], '--', label="1.26(b): cos(pi/3*t) Period T=6")

# Plot settings
plt.title("Signals HW1 Problem 1.26 Michael Rogers")
plt.xlabel('t (s)')
plt.legend()
plt.xlim(tMin, tMax)
plt.grid(linestyle=':')

# Save and Show Plot
plt.savefig("Signals_1-26.png")
plt.show()
plt.clf()