from EE_Calc import *
print()

db_gains = [3, 12, 18, 22]
gains = [vG(d) for d in db_gains]

def Rin(Rf, g):
    return Rf / (1 + g/2)

for g in gains:
    Rf = 100e3
    print("G: \t{:.1f}\tRin: \t{:.2f}".format(dBV(g), Rin(Rf, g)))

print('=======================================================================')

decs = range(32)
bins = [bits(d, True) for d in decs]

step = 2.2 / 32

for b, d in zip(bins, decs):
    print("{:>10}\t{:>4} V".format(b, d*step + 0.2))