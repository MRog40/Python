import matplotlib.pyplot as plt
import numpy as np

# Diameter of aperture in inches
diam = 5

# Size of projectile
proj = 0.177

def distance( x ):
    return ((11.547)/(1.155 * ( np.sqrt(6.25 - x**2) + 5 ))) * proj

dist_x = np.linspace(0, 5, 1000)
distribution = [ 1/distance(x) for x in np.linspace(0, 2.5, num=1000) ]

sensors = []

x = 0

while ( x < 100 ):
    sensors.append(x)
    x += distance(x)


[print(x) for x in sensors]

#plt.plot(dist_x, distribution, "b", label="Distribution")
plt.plot( sensors, [0 for i in sensors], ".r", label="Sensor" ) 

plt.title("Sensor Distribution")

plt.xlabel("Position from Center (in)")
plt.ylabel("")

plt.legend()


plt.show()

