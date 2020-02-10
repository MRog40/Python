import matplotlib.pyplot as plt
import numpy as np
from math import floor, log10

# Functions
def phase(theta):
    return np.exp(1j*np.deg2rad(theta))
def wye2delta(wye_load):
    return wye_load * 3
def delta2wye(delta_load):
    return delta_load / 3
def powerise10(x):
    """ Returns x as a*10**b with 0 <= a < 10
    """
    if x == 0: return 0,0
    Neg = x < 0
    if Neg: x = -x
    a = 1.0 * x / 10**(floor(log10(x)))
    b = int(floor(log10(x)))
    if Neg: a = -a
    return a,b
def eng(x):
    """Return a string representing x in an engineer friendly notation"""
    a,b = powerise10(x)
    if -3 < b < 3: return "%.6g" % x
    a = a * 10**(b % 3)
    b = b - b % 3
    return "%.6gE%s" % (a,b)
def printphasor(x):
    A = abs(x)
    B = np.rad2deg(np.angle(x))
    return eng(A) + " ∠ " + "%.2f" % B + "°"
def printrect(x):
    A = np.real(x)
    B = np.imag(x)
    if (B != 0):
        return eng(A) + " + j" + eng(B)
    else:
        return eng(A)
def parallel_wye(wye1, wye2):
    wye_parallel = (wye1 * wye2)/((wye1 + wye2))
    return wye_parallel
pi = 3.141592654

# Input Variables
V_an = 240 / np.sqrt(3) * phase(30)
Z_y = 2.5 * phase(36.87)
Z_d = 5 * phase(-20)
Z_line = 0.09 + 0.000424*60*pi*2j

# Calculate total load and current
Z_load = parallel_wye(Z_y, delta2wye(Z_d))
I_la = V_an / (Z_load + Z_line)

# Final Calculations
V_ay = I_la * Z_load
V_AB = V_ay*np.sqrt(3)*phase(30)
V_line_drop = I_la * Z_line
I_ay = V_ay / Z_y
W_ay = 3*V_ay*np.conjugate(I_ay)
W_tl = 3*V_line_drop*np.conjugate(I_la)
W_gen = 3*V_an*np.conjugate(I_la)

# Print Results
print("\nV_ab at Loads: " + printphasor(V_AB) + " V")
# c
print("V_line_drop: " + printphasor(V_line_drop) + " V")
# d, e
print("W_ay: " + printrect(W_ay) + " W")
# f, g
print("W_tl: " + printrect(W_tl) + " W")
# h, i
print("W_gen: " + printrect(W_gen) + " W")
