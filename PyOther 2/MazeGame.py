import os
import msvcrt as ms

# set starting point
x = 0
y = 0
boardSize = 20

# Initialize blank maze
maze = [[i for i in '   '*boardSize] for j in range(boardSize)]

maze[y][x] = u'\uA19C'

def move(maze, key):
	global x, y
	maze[y][x] = ' '
	if key == 'W':
		if y == 0:
			return 'eb'
		else: y -= 1
	elif key == 'S':
		if y == len(maze)-1:
			return 'eb'
		else: y += 1
	elif key == 'D':
		if x == len(maze[0])-1:
			return 'eb'
		else: x += 1
	elif key == 'A':
		if x == 0:
			return 'eb'
		else: x -= 1
	else: return 'ik'
	maze[y][x] = u'\uA19C'
	return maze

def printArr(maze):
	print('\n'.join([''.join([item for item in row]) for row in maze]))

while True:
	printArr(maze)
	print("Make your move (W, A, S, D)", end='')
	key = ms.getch().decode()
	os.system('cls')
	new_maze = move(maze, key.upper())
	if new_maze == 'eb':
		print('Invalid Move: Edge of Board')
		maze[y][x] = u'\uA19C'
	elif new_maze == 'ik':
		print('Invalid Key: ' + key.upper())
		maze[y][x] = u'\uA19C'
	else:
		maze = new_maze
