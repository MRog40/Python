import numpy as np
import matplotlib.pyplot as plt

f1 = 2086870
f2 = 4913130
numHarms = 10

harm1 = [f1]
for i in range(2, numHarms+1):
	harm1.append(f1*i)

harm2 = [f2]
for i in range(2, numHarms+1):
	harm2.append(f2*i)

results = []
harmonics = []
for one in harm1:
	for two in harm2:
		results.append(one + two)
		harmonics.append("m: " + str(one/f1) + " n: " + str(two/f2) + " + ")
		results.append(one - two)
		harmonics.append("m: " + str(one/f1) + " n: " + str(two/f2) + " 1 - 2 ")
		results.append(two - one)
		harmonics.append("m: " + str(one/f1) + " n: " + str(two/f2) + "  2 - 1 ")

result = [freq for freq in results if 0.5e6 < freq < 7e6]

print()
print(len(result))
print()
print(result)
print(harmonics)

plt.hist(result, bins=1000)
plt.title('Harmonic Frequency Distributions with ' + str(numHarms))
plt.xscale('log')
plt.xlim(0.5e6, 7e6)
plt.show()