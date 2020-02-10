import matplotlib.pyplot as plt
import numpy as np
sqrt = np.sqrt
real = np.real
imag = np.imag
j = 1j

plt.rcParams["font.family"] = "Times New Roman"

# Michael Rogers Torque Speed Characteristic Plot in Python
# Energy Systems Problem 6-20
# Constants
r1 = 11.91
x1 = 44.68
r2 = 17.97
x2 = 44.68
xm = 210/2.15 - x1
v_phase = 210 / sqrt(3)
n_sync = 1795
w_sync = 94

# Calculate the Thevenin voltage and impedance
v_th = v_phase * (xm / sqrt(r1**2 + (x1 + xm)**2))
z_th = ((j*xm) * (r1 + j*x1))/(r1 + j*(x1 + xm))
r_th = real(z_th)
x_th = imag(z_th)

# Calculate all the speeds at varying slip
s = np.arange(0.003, 0.058, 0.001)
nm = (1 - s) * n_sync

# Calculate torque versus speed
t_ind = []
for ii in np.arange(0, len(s)):
	t_ind.append((3 * v_th**2 * r2 / s[ii]) / (w_sync * ((r_th + r2/s[ii])**2 + (x_th + x2)**2)))

print("T_start: " + str(t_ind[1]))

# Plot the torque-speed curve
plt.plot(nm,t_ind,'-k')
plt.xlabel(r'$\itn_{m}$')
plt.ylabel(r'$\tau_{ind}$')
plt.title (r'Lab 5 Induction Motor Torque-Speed Characteristic')
plt.grid()
plt.show()