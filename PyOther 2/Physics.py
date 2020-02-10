# Script for simulating a trebuchet
import numpy as np
import matplotlib.pyplot as plt

# Constants
PI = 3.141592654
GRAV = 9.81
FIXED = -1
TICKRATE = 100
 
# Functions
sqrt = np.sqrt
def tan(x): return np.tan(PI*x/180)
def arctan(x): return 180*np.arctan(x)/PI
def cos(x): return np.cos(PI*x/180)
def arccos(x): return 180*np.arccos(x)/PI
def sin(x): return np.sin(PI*x/180)
def arcsin(x): return 180*np.arcsin(x)/PI

def distance(one, two):
    return sqrt((one.x-two.x)**2 + (one.y-two.y)**2)


class object:
    def __init__(self, x, y, xv, yv, mass):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.mass = mass
        self.force = force(0, 0)

    @property
    def angle(self):
        return arctan(self.yv/self.xv)

    @property
    def velocity(self):
        return sqrt(self.xv**2 + self.yv**2)

class link:
    def __init__(self, one, two):
        self.length = distance(one, two)
        self.one = one
        self.two = two

    @property
    def angle(self):
        return arctan((self.one.y - self.two.y)/(self.one.x - self.two.x))

class force:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return force(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return force(self.x - other.x, self.y - other.y)

    @classmethod
    def fa(cls, mag, angle):
        cls.x = mag*cos(angle)
        cls.y = mag*sin(angle)
        return force(cls.x, cls.y)

    @property
    def angle(self):
        return arctan(self.y/self.x)

    @property
    def magnitude(self):
        return sqrt(self.xv**2 + self.yv**2)


def simulate(time, links):
    xpos = []
    for x in np.arange(0, time, 1/TICKRATE):
        for link in links:
            # Here, solve the pendulum
            gravity = - link.two.mass * GRAV
            link.two.force += force(0, gravity) # Force of gravity
            link.two.force += force.fa(-gravity*sin(link.angle), link.angle)
            link.two.xv += link.two.force.x / link.two.mass
            link.two.yv += link.two.force.y / link.two.mass
            link.two.x += link.two.xv/TICKRATE
            link.two.y += link.two.yv/TICKRATE
        xpos.append(link.two.x)
    
    plt.plot(np.arange(0, time, 1/TICKRATE), xpos)
    plt.show()

mass = 8 / 2.2

pendulum = object(-1, 0, 0, 0, mass)
hook = object(0, 2, 0, 0, FIXED)

links = [link(hook, pendulum)]


simulate(10, links)
