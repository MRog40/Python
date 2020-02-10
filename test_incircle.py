import matplotlib.pyplot as plt
import numpy as np

pi = 3.141592654

diam = 5

height = diam / 2 * 3

sqrt = np.sqrt

def triangle( x ):
    if x < 0:
        return height + x * 2
    if x >= 0:
        return height - x * 2

def circle( x ):
    return diam/2 - sqrt( (diam/2)**2 - x**2 )

xs = np.linspace(-height/sqrt(3), height/sqrt(3), 1000)

tri = [triangle( x ) for x in xs]
cir = [circle( x ) for x in xs]

plt.plot(xs, tri, "g", label="Triangle" ) 
plt.plot(xs, cir, "r", label="Circle" ) 

plt.show()
