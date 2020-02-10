import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

Is = 691.44*10**(-18)

def Vdiode(x):
    return 0.025*np.log(x+1)

def Vi(Vo):
    I3 = Vo/10000 + (0.001-(Vo/10000))/2
    Vd1x = (0.001-Vo/10000)
    return Vo + Vdiode(I3/Is) - Vdiode(Vd1x/(2*Is))

# Set Params
Vo = [-12, -11, -10.5, -9.99, -9.9, -9, -5, -2, -1, 0, 1, 2, 5, 9, 9.9, 9.99, 10.5, 11, 12]

for v in Vo:
    print("Vo: " + str(v) + "   Vi: " + str(round(Vi(v), 3)))

# File Output Info
title = "Tron 4.52 VTC"
xlabel = "Vi"
ylabel = "Vo"

# Plot data     "-","--","-.",":"
plt.plot([Vi(v) for v in Vo], Vo)

# Plot settings
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Save and Show Plot
plt.show()
