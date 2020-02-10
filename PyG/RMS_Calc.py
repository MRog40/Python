# Michael Rogers
# Parse ADC Capture data to find the RMS value
import numpy as np
import matplotlib.pyplot as plt

voltage = []

def data_median(data):  # Return the data list and median from paste
    for line in data.splitlines():
        if '\t' in line and '.' in line and not 'NaN' in line:
            voltage.append(float(line[line.index('\t')+1:]))
    return voltage, np.median(voltage)

def rms_level(data): # Return the noise level
    voltage, median = data_median(data)
    # Return the Square Root of the Mean of the Squares
    return np.sqrt(np.mean([(v - median)**2 for v in voltage]))

data = """
"""
print('\nRMS Level: {:.2f} \u00B5V'.format(rms_level(data)))