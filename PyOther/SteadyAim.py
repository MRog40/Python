import math
import numpy as np
import matplotlib; import matplotlib.pyplot as plt

ADC6 = range(-1, 32)
ADC5 = range(-1, 16)

# Plot data
for x in ADC6:
    plt.scatter([i/0.32 for i in [x]*33], [y/0.32 for y in ADC6], c='r', s=0.1)

plt.scatter(0,0, c='r', label="6-Bit ADC")

matplotlib.patches.Circle((0,0), radius=10)

plt.xlim(0,100)
plt.ylim(0, 100)
plt.xlabel("X-Stick %")
plt.ylabel("Y-Stick %")
plt.title("Steady Aim Idea")
plt.legend()
plt.show()