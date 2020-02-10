import matplotlib.pyplot as plt
import numpy as np
from math import floor, log10
import cmath

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
V_an = 248*phase(45)
Z_y = 1 + 1j
Z_d = -2j
Z_line = 0.1j

# Calculate Voltages
V_bn = V_an*phase(-120)
V_cn = V_an*phase(120)
V_ab = np.sqrt(3)*V_an*phase(30)
V_bc = V_ab*phase(30)
V_ca = np.sqrt(3)*V_an*phase(30)

# Calculate Currents
#####
Z_load = parallel_wye(Z_y, delta2wye(Z_d))
# print("\nZ_load: " + printrect(Z_load))
# print("Z_eq: " + printrect(Z_load + Z_line))
#####
I_la = V_an / (Z_load + Z_line)
I_lb = V_bn / (Z_load + Z_line)
I_lc = V_cn / (Z_load + Z_line)

# Calculate Powers // Each phase is for A (top)
W_gen = V_an*np.conjugate(I_la)
W_phase = (V_an - I_la * Z_line)*np.conjugate(I_la)
P_gen = np.real(W_gen)
P_phase = np.real(W_phase)
Q_gen = np.imag(W_gen)
Q_phase = np.imag(W_phase)
S_gen = abs(W_gen)
S_phase = abs(W_phase)
pf_gen = P_gen / S_gen
pf_phase = P_phase / S_phase

# Results
# print("\nI_La: " + printphasor(I_la) + " A")
# print("I_Lb: " + printphasor(I_lb) + " A")
# print("I_Lc: " + printphasor(I_lc) + " A")
# print("V_AB: " + printphasor(V_ab) + " V")
# print("V_BC: " + printphasor(V_bc) + " V")
# print("V_CA: " + printphasor(V_ca) + " V")
# print("W_gen: " + printrect(W_gen) + " W")
# print("W_phase: " + printrect(W_phase) + " W")
# print("S_gen: " + printrect(S_gen) + " VA")
# print("S_phase: " + printrect(S_phase) + " VA")
# print("pf_gen: " + printrect(pf_gen))
# print("pf_phase: " + printrect(pf_phase))

# Find Y Load Phase Voltages
print("\nV_an across Y load: " + printphasor(I_la * Z_load) + " V")
print("V_bn across Y load: " + printphasor(I_lb * Z_load) + " V")
print("V_cn across Y load: " + printphasor(I_lc * Z_load) + " V")

# Find Delta Load Phase Voltages
V_ab_d = (I_la * Z_load)*np.sqrt(3)*phase(30)
#print("\nV_ab at Delta Load: " + printphasor(V_ab_d) + " V")

V_bc_d = (I_lb * Z_load)*np.sqrt(3)*phase(30)
#print("V_bc at Delta Load: " + printphasor(V_bc_d) + " V")

V_ca_d = (I_lc * Z_load)*np.sqrt(3)*phase(30)
#print("V_ca at Delta Load: " + printphasor(V_ca_d) + " V")

# Find Delta Load Phase Currents
I_ab_d = V_ab_d / Z_d
print("\nI_ab at Delta Load: " + printphasor(I_ab_d) + " A")

I_bc_d = V_bc_d / Z_d
print("I_bc at Delta Load: " + printphasor(I_bc_d) + " A")

I_ca_d = V_ca_d / Z_d
print("I_ca at Delta Load: " + printphasor(I_ca_d) + " A")

