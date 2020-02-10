# Michael Rogers
# Find and plot the AC Characteristic of the amplifier
import numpy as np
import matplotlib.pyplot as plt

# User data --------------------------------------------------------------------

# Data file, frequency, amplitude of input in microvolts
# Frequency, THS, VCA_5ks, VCA_1ks, VCA_Buffer
data = [
    [20000.0, 354.6, 112.2],
    [24800.0, 362.5, 114.8],
    [30800.0, 367, 116.2],
    [38200.0, 371, 117.5],
    [47400.0, 373.1, 118.1],
    [58900.0, 375, 118.7],
    [73000.0, 376.5, 119.3],
    [90600.0, 376.5, 119.3],
    [112500.0, 377.2, 119.5],
    [139600.0, 378.4, 120],
    [173200.0, 378.6, 120.1],
    [214900.0, 378.6, 120.1],
    [266700.0, 378.2, 120.3],
    [331000.0, 377.33, 120.2],
    [410700.0, 374.2, 119.7],
    [509700.0, 369.4, 118.8],
    [632500.0, 361.7, 117.2],
    [784900.0, 353.4, 116],
    [974100.0, 340.5, 113.6],
    [1208800.0, 258.3, 88.1],
    [1240000.0, 185.5, 63.5],
]
data = np.array(data)

# Plot Label Information
label = 'Port (THS + 10dB)'
style = 'o-r' # Similar to matlab styling
label2 = 'Starboard (THS)'
style2 = 'o-k'

# Font Settings
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 26})

# Plot Info
title = "AC Characteristic of Reciever"
xlabel = "Frequency (Hz)"
ylabel = "Amplitude (dB)"

plt.plot(data[:,0], [20*np.log10(v/18) for v in data[:,1]], style, markersize=2, label=label)
plt.plot(data[:,0], [20*np.log10(v/18) for v in data[:,2]], style2, markersize=2, label=label2)

# Apply plot info
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend(fontsize=14)
plt.grid(True, which="both")

# Log the frequency axis
plt.semilogx()
plt.show()
