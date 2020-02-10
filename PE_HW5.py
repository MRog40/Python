from EE_Calc import *
empty()

# Buck-Boost Converter Params
Vin = 12
D = 0.6
fs = 400e3
Po = 36
L = 25e-6

Ts = 1/fs

Vo = Vin * D / (1-D)
print("Vo: {:.2f}".format(Vo))

Io = Po/Vo

di_L = 1/L * Vin * D * Ts
print("di_L: {:.3f}".format(di_L))

IL = Io / (1-D)
print("IL: {:.3f}".format(IL))

Io = 0.36 * (1-D)
print(Io*Vo)
#####################################################
Po = 5
I_L = Po/(Vo * (1-D))

print("I_L: ", I_L)

print("L: ", engu(1/(2*I_L)*Vin*D*Ts, 'H'))

#####################################################
print('='*40,"\n")

Vin = 9
Vo = 18
Po = 5
D = Vo/(Vin + Vo)
I_L = Po/(Vo * (1-D))
print("9V L: ", end="")
engu(1/(2*I_L)*Vin*D*Ts, 'H')

Vin = 15
Vo = 18
Po = 5
D = Vo/(Vin + Vo)
I_L = Po/(Vo * (1-D))
print("15V L: ", end="")
engu(1/(2*I_L)*Vin*D*Ts, 'H')

print("="*50, "\n")
print("="*50, "\n")

I_rated = 1200
Vin= 650
Vo = 900
D = (Vo - Vin)/Vo
fs = 50e3
Ts = 1/fs
di_L = 0.1 * I_rated
I_L = di_L / 2
print("650V L: ", end="")
engu(1/(2*I_L)*Vin*D*Ts, 'H')

print("*"*60)

L = 1/(2*I_L)*Vin*D*Ts
Vin= 500
Vo = 900
D = (Vo - Vin)/Vo
print("D: ",D)
fs = 50e3
Ts = 1/fs
di_L = 1/L * Vin * D * Ts
print("di_L = ", di_L)

print("*"*70)

Vin= 800
Vo = 900
D = (Vo - Vin)/Vo
print("D: ", D)
fs = 50e3
Ts = 1/fs
di_L = 1/L * Vin * D * Ts
print("di_L = ", di_L)
