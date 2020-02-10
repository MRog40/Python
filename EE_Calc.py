# Batch file
# python -i C:/Users/7258163/Documents/Python_Scripts/EE_Workspace.py %*
# Exe Command
# C:\Windows\System32\cmd.exe /k C:\Users\7258163\Documents\EE_Workspace.bat

def printheader():
    #text = r"""     ____________   ______      __    
    #/ ____/ ____/  / ____/___ _/ /____
   #/ __/ / __/    / /   / __ `/ / ___/
  #/ /___/ /___   / /___/ /_/ / / /__  
 #/_____/_____/   \____/\__,_/_/\___/   """
    #print(text)
    return

# LIBRARIES
import os
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from TimeClass import *

# WINDOW CONTROL FUNCTIONS
def clc():
    os.system('cls')
    printheader() # Clear the command line
clear = clc # Equivalent

def empty():
    os.system('cls')

def varList():
    print([item for item in dir() if not item.startswith("__")])
    # print("\nCurrent Variables\n-----------------")
    # for variable in dir()[index:]:
    #     print(variable)

clc()

# BASIC MATH FUNCTIONS
pi = np.pi
log = np.log10
sqrt = np.sqrt
sin = np.sin
cos = np.cos
tan = np.tan
acos = np.arccos
asin = np.arcsin
atan = np.arctan
ln = np.log
exp = np.exp
angle = np.angle
roots = np.roots
mean = np.mean
median = np.median

# CONSTANTS
j = 1j
c = 2.99792458129e8
epsilon = 8.85418782e-12
mu = pi*4e-7
k_b = 1.380649e-23

# MATLAB SUBSTITUTE FUNCTIONS
plot = plt.plot; plt.show
range = np.arange
solve = sp.solveset
def syms(vars):
    items = []
    for var in vars:
        items.append(sp.Symbol(var))
    return items
def symbolics():
    pi = sp.pi
    sqrt = sp.sqrt
    sin = sp.sin
    cos = sp.cos
    tan = sp.tan
    acos = sp.acos
    asin = sp.asin
    atan = sp.atan
    ln = sp.log
    exp = sp.exp
    roots = sp.roots
    expand = sp.expand
    trigsimp = sp.trigsimp
    simplify = sp.simplify

# UNIT CONVERSION
def ft2meter(feet):
    return feet*0.3048 # Convert feet to meters
def meter2ft(meter):
    return meter/0.3048 # Convert meters to feet

def F2C(F):
    return (F - 32) * 5/9 # Convert Fahrenheit to Celsius
def C2F(C):
    return (C * 9/5) + 32 # Convert Celsius to Fahrenheit

rad2deg = np.rad2deg # Convert radians to degrees
deg2rad = np.deg2rad # Convert degrees to radians

# FORMAT PRINT FUNCTIONS
def eng(x):
    print(EngNumber(x)) # Print number using engineering format

def engu(x, units = 'V'):
    print(str(EngNumber(x)) + str(units)) # Print number using engineering format and units

def printphase(complex, newline = True):
    print(round(abs(complex),4), end = '')
    print(u'\u2220', end = '')
    print(round(rad2deg(angle(complex)),2), end = '')
    if newline:
        print(u'\u00B0', end = '\n')
    elif not newline:
        print(u'\u00B0', end = '') # Print phasor format of complex number

def EngNumber(obj, digits=5):
    unitMap = {'Y':1e24, 'Z':1e21, 'E':1e18, 'P':1e15, 'T':1e12, 'G':1e9, 'M':1e6, 
    'k':1e3, '':1, 'm':1e-3, 'u':1e-6, 'n':1e-9, 'p':1e-12, 'f':1e-15, 'a':1e-18, 'z':1e-21, 'y':1e-24};

    for unit, value in unitMap.items():
        if(obj >= value*100):           # TODO: More elegant solution for this
            return removeZeros(str(round((obj / value), digits - 3))) + unit
        elif(obj >= value*10):
            return removeZeros(str(round((obj / value), digits - 2))) + unit
        elif(obj >= value):
            return removeZeros(str(round((obj / value), digits - 1))) + unit # Used internally, equivalent to eng()

def removeZeros(obj):
    if(obj[-1] == '.' and obj[-2] == '0'):
        return obj[0:-1]
    elif((obj[-1] == '0' or obj[-1] == '.')):
        return removeZeros(obj[0:-1]) # Recursion! v cool
    else:
        return obj # Used Internally to remove trailing zeros

# ELECTRICAL ENGINEERING FUNCTIONS
def para(*args):
    s = 0 # sum
    for arg in args: # If arg is list, sum list, else just add the arg
        if isinstance(arg, (list,)):
            s += sum([1/a for a in arg])
        else:
            s += 1/arg 
    return 1/s # Return the product over the sum of all args

def avg(*args):
    s = 0 # sum
    c = 0 # count
    for arg in args: # If arg is list, sum list, else just add the arg
        if isinstance(arg, (list,)):
            s += sum([a for a in arg])
            c += len(arg)
        else:
            s += arg 
            c += 1
    return s/c # Return the average of all args

def addRMS(*args):
    return np.sqrt(sum([arg**2 for arg in args])) # Return the square root of the sum of the squares

def jnNoise(resistance):
    return engu(sqrt(4*k_b*300*resistance), 'V/\u221aHz') # Return the thermal noise at room temperature (300 K) in Vrms per root Hz

def bits(num, string=False):
    if not string:
        print(len(bin(num)[2:]))
        print(bin(num)[2:]) # Print the number of bits and the bin
    else:
        return str(bin(num)[2:])

def data_median(data): # Find the median value of an entire dataset
    voltage = []
    for line in data.splitlines()[1:]:
        if '\t' in line:
            voltage.append(float(line[line.index('\t')+1:]))
    return np.median(voltage)

def dB(ratio):
    return 10*log(ratio) # Return the dB value of a ratio

def dBV(ratio):
    return 20*log(ratio) # Return the dB value of a voltage or pressure ratio

def vP(dB):
    return 10**(dB/10) # Return the power gain given dB

def vG(dB):
    return 10**(dB/20) # Return the voltage gain given dB

def fC(r, c, use=0):
    if use is 0:
        engu(fC(r, c, 1), 'Hz')
    else:
        return 1/(2*pi*r*c) # Return the cutoff frequency given resistance and capacitance

def res(l, c):
    return 1/(2*pi*np.sqrt(l*c)) # Resonant frequency given inductance and capacitance

def phase(degrees):
    radians = deg2rad(degrees)
    return cos(radians) + j*sin(radians) # Phasor equivalent to angle symbol in degrees

def inputImp(Zl, Zo, Bl): # TODO
    return "TODO"

def Bl(f, Vp): # TODO
    return "TODO"

def reflectionCoeff(Zl, Zo):
    return (Zl-Zo)/(Zl+Zo) # Reflection coefficient from load and characteristic impedance

def VSWR(gamma):
    return (1+abs(gamma))/(1-abs(gamma)) # Standing wave ratio from reflection coefficient

def shuntStubImpOC(Zo, Bl):
    return -j*Zo/tan(Bl) # Shunt Open Circuit Stub Impedance

def shuntStubImpSC(Zo, Bl):
    return -j*Zo*tan(Bl) # Shunt Short Circuit Stub Impedance

def hex2rgb(hex):
    if hex[0] is '#':
        hex = hex[1:]
    if len(hex) is 3:
        print('rgb(' + str((int(hex[0], 16)*16 + 15)) + ', ' 
            + str((int(hex[1], 16)*16 + 15)) + ', ' + str((int(hex[2], 16)*16 + 15)) + ')')
        print(str((int(hex[0], 16)*16 + 15)) + str((int(hex[1], 16)*16 + 15)) + str((int(hex[2], 16)*16 + 15)))
    else:
        print('rgb(' + str(int(hex[0:2], 16)) + ', ' 
            + str(int(hex[2:4], 16)) + ', ' + str(int(hex[4:6], 16)) + ')')
        print(str(int(hex[0:2], 16)) + str(int(hex[2:4], 16)) + str(int(hex[4:6], 16))) # Convert hex to RGB color

# HELP SECTION
def help():
    text = r"""   _____     __      __ __    __   
  / ___/__ _/ /___  / // /__ / /__ 
 / /__/ _ `/ / __/ / _  / -_) / _ \
 \___/\_,_/_/\__/ /_//_/\__/_/ .__/
                          /_/    """
    print('\n' + text)


# Workspace
