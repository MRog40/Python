# Michael Rogers
# Find and plot the AC Characteristic of the amplifier
import numpy as np
import matplotlib.pyplot as plt

# User data --------------------------------------------------------------------

# Data file, frequency, amplitude of input in microvolts
# Frequency, THS, VCA_5ks, VCA_1ks, VCA_Buffer
data = [
    [20000, 56, 88, 60, 60, 57, 15.2],
    [25100, 57, 92, 62, 62, 60, 15.6],
    [31500, 58, 95, 64, 63, 62, 15.9],
    [39500, 59, 96, 65, 65, 63, 16.1],
    [49600, 59, 97, 65, 65, 64, 16.2],
    [62300, 59, 97, 65, 66, 64, 16.25],
    [78200, 60, 96, 65, 66, 64, 16.3],
    [98200, 60, 95, 65, 66, 64, 16.3],
    [123400, 60, 94, 65, 66, 64, 16.3],
    [154900, 60, 91, 65, 66, 64, 16.3],
    [194400, 60, 87, 64, 66, 64, 16.3],
    [244100, 60, 82, 63, 65, 64, 16.3],
    [306500, 60, 75, 61, 64, 63, 16.25],
    [384800, 60, 66, 59, 63, 62, 16.2],
    [483000, 60, 57, 56, 60, 60, 16.1],
    [606400, 59, 47, 51, 57, 58, 16.05],
    [761300, 58, 37, 45, 54, 54, 15.95],
    [955800, 57, 28, 38, 49, 48, 15.8],
    [1100000, 56, 24, 34, 46, 42, 15.65],
    [1200000, 49, 18, 27, 38, 34, 15.55]
]
data = np.array(data)

# Plot Label Information
label = 'Starboard (THS)'
style = 'o-k' # Similar to matlab styling
label2 = 'Port (VCA) 5k 470pFc 12pFd'
style2 = 'o-r'
label3 = 'Port (VCA) 1k 2.2nFc'
style3 = 'o-b'
label4 = 'Port (VCA) 5k 2.2nFc 5550 BJT Buffer'
style4 = 'o-g'
label5 = 'Port (VCA) \'\' 5089 Bootstrapped'
style5 = 'o-m'
label6 = 'Port (VCA) \'\' OScope Data'
style6 = 'o-c'

# Font Settings
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 26})

# Plot Info
title = "AC Characteristic of Reciever"
xlabel = "Frequency (Hz)"
ylabel = "Amplitude (dB)"

plt.plot(data[:,0], [20*np.log10(v/9.23) for v in data[:,1]], style, markersize=2, label=label)
plt.plot(data[:,0], [20*np.log10(v/9.23) for v in data[:,2]], style2, markersize=2, label=label2)
plt.plot(data[:,0], [20*np.log10(v/9.23) for v in data[:,3]], style3, markersize=2, label=label3)
plt.plot(data[:,0], [20*np.log10(v/9.23) for v in data[:,4]], style4, markersize=2, label=label4)
plt.plot(data[:,0], [20*np.log10(v/9.23) for v in data[:,5]], style5, markersize=2, label=label5)
plt.plot(data[:,0], [v for v in data[:,6]], style6, markersize=2, label=label6)

# Apply plot info
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend(fontsize=14)
plt.grid(True, which="both")

# Log the frequency axis
plt.semilogx()
plt.show()
