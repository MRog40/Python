# Michael Rogers
# Envelope Plotting Example
import numpy as np
import matplotlib.pyplot as plt

# Finding the envelope using the Hilbert transform
#   I was pointed in this direction by Ditigal Envelope Detection: The G, B, & U
#       By Richard Lyons -> Asynchronous Complex Envelope Detection
#   The hilbert transform is the complex component generated from the analytic
#   signal:
#       inverse FFT( FFT(signal) * 2 * Heaviside)
#   The envelope is the magnitude of the analytic signal
def envelope(signal):
    Fsignal = np.fft.fft(signal) # FFT(signal)
    frequencies = np.fft.fftfreq(len(signal)) # Get frequencies of the FFT
    Fsignal[np.where(frequencies <= 0)] = 0. # *Heaviside (filter neg freqs) # And 0 Hz to remove DC
    return np.abs(np.fft.ifft(Fsignal*2)) # inverse FFT of *2

# Generate Test Signal
voltage = np.array([100 * np.sin(5*t+2) * np.sin(2*t+1) * np.cos(70*t) for t in np.arange(0, 3, 0.001)])

# Process Signal
avg = np.mean(voltage)
voltage = voltage #- 15
env = envelope(voltage)
voltage = [v - avg for v in voltage]
env = [e - avg for e in env]
avg = np.mean(env)

# Plot Font Settings
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 16})

# Plot Labels
title = "Envelope Algorithm"
xlabel = "Time"
ylabel = "Microvolts"

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Plot the data
plt.plot(env, 'k', label='Envelope')
plt.plot(voltage, 'b', label='Raw Data')
plt.plot([avg for i in range(len(env))], 'r', label='Mean Envelope')

plt.legend(fontsize=12)
plt.show()