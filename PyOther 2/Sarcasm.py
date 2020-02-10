from numpy.random import choice
print('You: ' + ''.join([choice([x.upper(), x.lower()]) for x in input('What say you? ')]))