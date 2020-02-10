# Michael Rogers
# Find and plot the AC Characteristic of the amplifier
import numpy as np
import matplotlib.pyplot as plt

# User data --------------------------------------------------------------------

# Folder where the data is stored
root = 'C:\\Users\\rogersmichael\\Documents\\Python\\May31Data\\'

# Data file, frequency, amplitude of input in microvolts
data = [
    ['20kPort.txt', 20000, 60400],
    ['25_1kPort.txt', 25100, 59800],
    ['31_5kPort.txt', 31500, 59100],
    ['39_5kPort.txt', 39500, 58500],
    ['49_6kPort.txt', 49600, 58500],
    ['62_3kPort.txt', 62300, 57900],
    ['78_2kPort.txt', 78200, 57300],
    ['98_2kPort.txt', 98200, 57300],
    ['123_4kPort.txt', 123400, 57300],
    ['154_9kPort.txt', 154900, 57300],
    ['194_4kPort.txt', 194400, 57300],
    ['244_1kPort.txt', 244100, 57300],
    ['306_5kPort.txt', 306500, 57300],
    ['384_4kPort.txt', 384800, 57300],
    ['483kPort.txt', 483000, 57900],
    ['606_4kPort.txt', 606400, 57900],
    ['761_3kPort.txt', 761300, 58500],
    ['955_8kPort.txt', 955800, 58500],
    ['999_9kPort.txt', 999900, 59100]
]
# Plot Label Information
label = 'Port (Modified)'
style = 'o-k' # Similar to matlab styling

data2 = [
    ['20kStar.txt', 20000,  60400],
    ['25_1kStar.txt', 25100,  59800],
    ['31_5kStar.txt', 31500,  59100],
    ['39_5kStar.txt', 39500,  58500],
    ['49_6kStar.txt', 49600,  58500],
    ['62_3kStar.txt', 62300,  57900],
    ['78_2kStar.txt', 78200,  57300],
    ['98_2kStar.txt', 98200,  57300],
    ['123_4kStar.txt', 123400,  57300],
    ['154_9kStar.txt', 154900,  57300],
    ['194_4kStar.txt', 194400,  57300],
    ['244_1kStar.txt', 244100,  57300],
    ['306_5kStar.txt', 306500,  57300],
    ['384_4kStar.txt', 384800,  57300],
    ['483kStar.txt', 483000,  57900],
    ['606_4kStar.txt', 606400,  57900],
    ['761_3kStar.txt', 761300,  58500],
    ['955_8kStar.txt', 955800,  58500],
    ['999_9kStar.txt', 999900,  59100]
]
label2 = 'Starboard (Original)'
style2 = 'o-r'

# Functions --------------------------------------------------------------------

# Finding the envelope using the Hilbert transform
#   I was pointed in this direction by Ditigal Envelope Detection: The G, B, & U
#       By Richard Lyons -> Asynchronous Complex Envelope Detection
#   The hilbert transform is the complex component generated from the a-signal
# The envelope is the magnitude of the analytic signal
# Analytic signal: inverse FFT(FFT(signal) * 2 * Heaviside)
def envelope(signal):
    Fsignal = np.fft.fft(signal)  # FFT(signal)

    # Get each frequency contained in the signal
    frequencies = np.fft.fftfreq(len(signal))  # Get frequencies of the FFT

    # At each index where the frequency is negative, set the magnitude to zero
    Fsignal[np.where(frequencies < 0)] = 0.  # *Heaviside

    return np.abs(np.fft.ifft(Fsignal*2))  # magnitude of inverse FFT of *2

# Main
def plot_data(data, plot_style, plot_label):
    # List initialization
    files = [row[0] for row in data]  # All of the filenames
    frequencies = [row[1] for row in data]  # All of the frequencies
    input_mags = [row[2] for row in data]  # The input peak from the scope
    signals = []  # List of numpy arrays, each signal from loading file
    envelopes = []  # '', the envelope of the signal
    amplitudes = []  # The mean amplitude of each envelope

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
        dc = np.mean(signal) # Find the DC of the signal to remove later
        env = envelope(signal) # Find the envelope of the signal
        signal = [v - dc for v in signal] # Remove the DC from the signal
        env = [e - dc for e in env] # Remove the DC from the envelope
        envelopes.append(envelope(signal)) # Add the envelope to envelopes
        amplitudes.append(np.mean(env)) # Add the avg envelope to amplitudes

    # Plot the data
    plt.plot(frequencies, [20*np.log10(amp/input) for amp, input in zip(amplitudes,
        input_mags)], plot_style, markersize=2, label=plot_label)


# Script -----------------------------------------------------------------------

# Font Settings
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 26})

# Plot Info
title = "AC Characteristic of Reciever"
xlabel = "Frequency (Hz)"
ylabel = "Enveloped Amplifier Gain (dB)"

plot_data(data, style, label)
plot_data(data2, style2, label2)

# Apply plot info
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend(fontsize=14)
plt.grid(True, which="both")

# Log the frequency axis
plt.semilogx()
plt.show()
