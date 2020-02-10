# Script for simulating a trebuchet
import numpy as np

# Constants
PI = 3.141592654
GRAV = 9.81
FIXED = -1
TICKRATE = 100

# Functions
sqrt = np.sqrt
def tan(x): return np.tan(180*x/PI)
def arctan(x): return 180*np.arctan(x)/PI
def cos(x): return np.cos(180*x/PI)
def arccos(x): return 180*np.arccos(x)/PI
def sin(x): return np.sin(180*x/PI)
def arcsin(x): return 180*np.arcsin(x)/PI
def distance(one, two):
    return sqrt((one.x-two.x)**2 + (one.y-two.y)**2)

class object:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class link:
    def __init__(self, one, two):
        self.length = distance(one, two)
        self.one = one
        self.two = two

    @property
    def angle(self):
        return arctan((self.one.y - self.two.y)/(self.one.x - self.two.x))

onthe = object(0, 0)
twothe = object(1, 1)

print(link(onthe, twothe).angle)