# Michael Rogers
# text frame animation test
import time
import numpy as np
import random
import os

frame = [[i for i in '   '*40] for j in range(20)]

def newFrame(frame):
	newFrame = np.roll(frame, -2, axis=1)
	block = int(20 * random.random())
	chance = int(10 * random.random())
	if chance is 1:
		newFrame[block][-1] = u'\uA19C'
	return newFrame

def displayFrame(frame):
	os.system('cls')
	print('\n'.join([''.join([item for item in row]) for row in frame]))

while True:
	displayFrame(frame)
	time.sleep(0.03)
	frame = newFrame(frame)