# Michael Rogers
import matplotlib.pyplot as plt
import random

max_rolls = 500
forgiveness = 0.1
trials = 100

# Roll dice x times
def rolls(x):
    rolls = [random.randint(1,6) + random.randint(1,6)]
    if(x > 1):
        for roll in range(0,x-1):
            rolls.append(random.randint(1,6) + random.randint(1,6))
    return rolls

def get_distribution(all_rolls):
    distribution = [0,0,0,0,0,0,0,0,0,0,0]
    for roll in all_rolls:
        distribution[roll-2] = distribution[roll-2] + 1
    return distribution

def check_normal(distribution):
    normal = 1
    for i in range(2,8):
        previous_val = distribution[i]
        if i < 5:
            if previous_val > distribution[i+1]:
                if distribution[i+1] > 0:
                    if (1 - previous_val / distribution[i+1]) > forgiveness:
                        normal = 0
        else:
            if previous_val < distribution[i+1]:
                if distribution[i+1] > 0:
                    if (1 - previous_val / distribution[i+1]) > forgiveness:
                        normal = 0
    return normal

normal_rolls = [0]
for num_rolls in range(1, max_rolls):
    normal_rolls.append(0)
    for trial in range(0,trials+1):
        normal_rolls[num_rolls] += check_normal(get_distribution(rolls(num_rolls)))
        print('rolls: ' + str(num_rolls) + ' trial: ' + str(trial))

plt.title("Dice Roll Normality")
plt.xlabel("Rolls in Game")
plt.ylabel("Games with normal dist (of " + str(trials) + " )")
#plt.xlim(5, max_rolls)
#plt.ylim()
plt.plot(range(1,max_rolls+1), normal_rolls, 'red', linewidth=1)
plt.show()
