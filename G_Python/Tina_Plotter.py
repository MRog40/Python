# Michael Rogers
# Plot Tina Data
import numpy as np
import matplotlib.pyplot as plt

# User data --------------------------------------------------------------------

# Folder where the data is stored
root = 'C:\\Users\\rogersmichael\\Documents\\Python\\June5\\'

# Data file, frequency, amplitude of input in microvolts
data = [
    ['999_9kPort.txt']
]

# Functions --------------------------------------------------------------------

# Main
def plot_data(data):
    # List initialization
    files = [row[0] for row in data]  # All of the filenames
    frequencies = [row[1] for row in data]  # All of the frequencies
    input_mags = [row[2] for row in data]  # The input peak from the scope
    signals = []  # List of numpy arrays, each signal from loading file

    # In this case, the first column, time, is not needed
    # Each file is generate by using 'Export to Excel' and saving the file as a tab
    #   delimited txt file with the name specified above
    for filename in files:
        _, signal = np.genfromtxt(
            root + filename,  # Folder directory + file name = absolute path
            dtype=float,  # Force floats (may not be necessary, haven't tested)
            skip_header=1,  # Skip the first line
            unpack=True,  # Transpose the data so it is more easily returned
        )
        signals.append(signal)

    # Process each signal
    for signal in signals:
        return

    # Plot the data
    plt.plot(frequencies, [20*np.log10(amp/input) for amp, input in zip(amplitudes,
        input_mags)], markersize=2)


# Script -----------------------------------------------------------------------

# Font Settings
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 26})

# Plot Info
title = "AC Characteristic of Reciever"
xlabel = "Frequency (Hz)"
ylabel = "Enveloped Amplifier Gain (dB)"

plot_data(data)

# Apply plot info
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend(fontsize=14)
plt.grid(True, which="both")

# Log the frequency axis
plt.semilogx()
plt.show()
