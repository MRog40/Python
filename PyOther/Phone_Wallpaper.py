# Michael Rogers
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image, ImageOps

darkGray = '#181A1F' #  rgb(33, 37, 43)
gray = '#2C313C' #  rgb(40, 44, 52)
commentColor = '#7f848e' #  rgb(127, 132, 142)
lightGray = '#abb2bf' #  rgb(171, 178, 191)
offWhite = '#f8fafd' #  rgb(248, 250, 253)
pink = '#ef596f' #  rgb(239, 89, 111)
purple = '#d058d9' #  rgb(208, 88, 217)
blue = '#61afef' #  rgb(97, 175, 239)
green = '#89ca78' #  rgb(137, 202, 120)
orange = '#e5c07b' #  rgb(229, 192, 123)
red = '#c24038' # rgb(194, 64, 56)

colors = [pink, blue, purple, orange, green]

fig = plt.figure()

# Set Params
tMin = 0.6
tMax = 16.6
Frequency = 1000 # of signal samples per t
Wave_freq = 1.5
Wave_freq2 = 2
Amp = 9
decay = -0.2
space = 8
squiggle = 10
lw = 0.8

ts = np.arange(tMin, tMax + 1 if isinstance(tMax, int) else tMax,1/Frequency)

def f(t, i):
    return Amp*math.exp(decay*t)*np.sin(Wave_freq * t - 2*i/space*math.pi)

for i in range(5):
	plt.plot(ts,[f(t, i) for t in ts], colors[i], linewidth = lw, zorder = 20 - 5*i)

# Plot settings
ax = plt.gca()
plt.xlim(tMin, tMax)
ax.set_facecolor(darkGray)
fig.patch.set_facecolor(darkGray)
for side in ['bottom', 'top', 'left', 'right']:
	ax.spines[side].set_color(darkGray)
ax.xaxis.label.set_color(darkGray)
ax.yaxis.label.set_color(darkGray)
ax.tick_params(axis='x', colors=darkGray)
ax.tick_params(axis='y', colors=darkGray)

# Save and Show Plot
plt.savefig("NewGRAYWallpaper.png", dpi = 500, facecolor = darkGray,bbox_inches = 'tight',pad_inches=0)

# Add border to image
img = Image.open("NewGRAYWallpaper.png")
img_with_border = ImageOps.expand(img,border=1000,fill=darkGray)
img_with_border.show()
img_with_border.save("NewGRAYWallpaperBORDER.png")
