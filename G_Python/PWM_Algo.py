import matplotlib.pyplot as plt
import numpy as np
import math

# Settings
gChirpMinDuty = 5
gChirpMaxDuty = 45
gChirpNumSteps = 10
min_Freq = 0.001
max_Freq = 0.01

# Global Declare
INCREMENT = True
DECREMENT = False
PWM_Period_Table0 = []
PWM_Duty_Table0 = []


# This is meant to mimic the code in the function, removing unnecessary stuff so
# I can quickly debug and ensure it is working correctly
def Calculate_CHIRP_Parameters():

    startVAL1 = (1/min_Freq)/2
    endVAL1 = (1/max_Freq)/2
    deltaVAL1 = ((startVAL1 - endVAL1) // (gChirpNumSteps-1))

    freqVAL1 = startVAL1

    chirpIteration0 = 0
    maxIterations0 = 0
    step = 1

    # This loop generates the table of frequencies
    while(True):
        PWM_Period_Table0.append(freqVAL1)
        maxIterations0 += 1

        if(True):
            step += 1
            if(step > gChirpNumSteps):
                break
            if(step == gChirpNumSteps):
                freqVAL1 = endVAL1
            else:
                freqVAL1 -= deltaVAL1
    
    dutyVAL3 = (PWM_Period_Table0[chirpIteration0] * gChirpMinDuty/100)
    dutyVAL2 = -dutyVAL3
    dutyVAL4 = -PWM_Period_Table0[chirpIteration0] - dutyVAL2
    dutyVAL5 = -dutyVAL4

    # Initialize algo to fill Duty Cycle table
    iterationDuty = gChirpMinDuty
    dutyStep = 1
    dutyDirection = INCREMENT
    dutyMaxIteration = 1

    chirpIteration0 = 0

    dutyMaxIteration = math.ceil(maxIterations0 / 2) - 1

    dutyStep = (gChirpMaxDuty - gChirpMinDuty ) / dutyMaxIteration

    # This loop generates the table of duty cycle values (VAL3)
    while(True):
        dutyVAL3 = (PWM_Period_Table0[chirpIteration0] * iterationDuty/100)
        PWM_Duty_Table0.append(dutyVAL3)
        chirpIteration0 += 1

        if(dutyDirection == INCREMENT):
            if(chirpIteration0 == dutyMaxIteration):
                iterationDuty = gChirpMaxDuty
                dutyDirection = DECREMENT
            else:
                iterationDuty += dutyStep
        else:
            if(chirpIteration0 == maxIterations0-1):
                iterationDuty = gChirpMinDuty
            elif(chirpIteration0 == maxIterations0):
                break
            else:
                iterationDuty -= dutyStep

    chirpIteration0 = 0

# This loop simulates the eFlexPWM Module uses comparisons like Fig 38-3 in the
# KV4x Reference Manual
def Run_PWM():
    # I'm doing this pythonicly, but in the actual code, the new table value is
    # Incremented by the PWM counter overflowing. This math takes place in that
    # Interrupt. Instead of simulating that, I'm just cycling through each value
    # In the table and generating the period from those values, but the logic
    # is identical
    for freqVAL1, dutyVAL3 in zip(PWM_Period_Table0, PWM_Duty_Table0):
        freqINIT = -freqVAL1
        dutyVAL2 = -dutyVAL3
        dutyVAL4 = freqINIT - dutyVAL2
        dutyVAL5 = -dutyVAL4

        # This loop again is done by the counter, counting from INIT up to VAL1
        # I am saying INIT = -VAL1, which may not be correct
        for count in range(round(freqINIT), round(freqVAL1)):

            if(count > dutyVAL2 and count < dutyVAL3):
                pwm_a.append(5)
            else:
                pwm_a.append(0)

            if(count > dutyVAL4 and count < dutyVAL5):
                pwm_b.append(0)
            else:
                pwm_b.append(5)
            tri.append(count)
            val2.append(dutyVAL2)
            val3.append(dutyVAL3)
            val4.append(dutyVAL4)
            val5.append(dutyVAL5)

pwm_a = []; pwm_b = []; tri = []; val2 = []; val3 = []; val4 = []; val5 = []

Calculate_CHIRP_Parameters()
Run_PWM()

plt.subplot(2, 1, 1)
plt.plot(pwm_a, 'k', label="PWM_A")
plt.plot(pwm_b, 'r', label="PWM_B")
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(tri, 'b', label="Counter")
plt.plot(val2, label="VAL2")
plt.plot(val3, label="VAL3")
plt.plot(val4, label="VAL4")
plt.plot(val5, label="VAL5")
plt.suptitle("PWM Algorithm Test")
plt.legend()
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()