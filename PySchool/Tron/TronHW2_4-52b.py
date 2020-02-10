import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

Is = 691.44*10**(-18)
Isource = 0.001

def Vdiode(x):
    return 0.025*np.log(x+1)

def I3(Vo):
    return Vo/10000 + (Isource-(Vo/10000))/2

def I1(Vo):
    return Isource - I3(Vo)

def Vi(Vo):
    Vd1x = (Isource-Vo/10000)
    return Vo + Vdiode(I3(Vo)/Is) - Vdiode(Vd1x/(2*Is))

# Set Params
Vo = [-12, -11, -10.5, -9.99, -9.9, -9, -5, -2, -1, 0, 1, 2, 5, 9, 9.9, 9.99, 10.5, 11, 12]

for v in Vo:
    print(str(v) + ", " + str(round(Vi(v), 4)) + ", " + str(I1(v)) + ", " + str(I3(v)))

# File Output Info
title = "Tron 4.52 VTC"
xlabel = "Vi"
ylabel = "Vo"

# Plot data     "-","--","-.",":"
#Vrange = np.arange(-12, 12, 0.00001)
#plt.plot([Vi(v) for v in Vrange], Vrange)

# Plot settings
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Save and Show Plot
#plt.show()
