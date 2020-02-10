# Michael Rogers
# Parse Data and Plot It
import numpy as np
import matplotlib.pyplot as plt

def old_parse_data(data_in, columns = 2, delimiter = '\t'):
    data_out = np.empty([columns, 0])
    for line in data_in.splitlines():
        if delimiter in line and not line.upper().isupper(): # If line contains tabs and not letters
            line.join('\t')
            row = np.empty(columns)
            for i in range(columns):
                row[i] = float(line[:line.index('\t')])
                print('\n\n {} \n\n'.format(row[i]))
                line = line[line.index('\t'):]
                print(line)
            np.vstack((data_out, row))
    return data_out

def parse_data(file):
    return np.transpose(np.loadtxt(file))

def data_median(data):  # Return the data list and median from paste
    voltage = []
    for line in data.splitlines():
        if '\t' in line and '.' in line and not 'NaN' in line:
            voltage.append(float(line[line.index('\t')+1:]))
    return voltage, np.median(voltage)


def rms_level(data): # Return the noise level
    voltage, median = data_median(data)
    # Return the Square Root of the Mean of the Squares
    return np.sqrt(np.mean([(v - median)**2 for v in voltage]))

# N = 19
# x = np.logspace(np.log10(20e3), np.log10(1.2e6), N)

# for num in x:
# 	print(num)

sweep = [
    (20000, 16317),
    (25108.23451, 16897),
    (31521.172, 17124),
    (39572.04893, 17230),
    (49679.21422, 17273),
    (62367.86804, 17427),
    (78297.35282, 17587),
    (98295.4148, 17642),
    (123401.2163, 17653),
    (154919.3338, 17411),
    (194487.5482, 17438),
    (244161.9484, 17216),
    (306523.773, 17056),
    (384813.5387, 16929),
    (483099.4285, 16441),
    (606488.6871, 16180.8),
    (761393.009, 15799),
    (955861.7112, 15258),
    (999900, 15120)
]

data = parse_data('data.txt')
print(data[0])
print(data[1])

freq, median = zip(*sweep)


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 26})

# Plot Data
title = "AC Characteristic of Reciever"
xlabel = "Frequency (Hz)"
ylabel = "Envelope Input Gain (dB)"

plt.plot(data[0], [20*np.log10(d/10000) for d in data[1]], 'o-r', markersize=2,
	label='experimental')
plt.semilogx()

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend()
plt.show()