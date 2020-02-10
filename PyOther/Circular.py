# Michael Rogers
from PIL import Image, ImageFilter
import tkinter as tk; from tkinter import filedialog
from tkinter.simpledialog import askstring, askinteger
from tkinter.messagebox import showerror

# Select and Load the image
tk.Tk().withdraw()
file_path = tk.filedialog.askopenfilename()
img = Image.open(file_path)

# Get user input for screen resolution
new_h = 2880
new_w = 1440
colors = ['#FFC30F', '#FF5733','#C70039','#900C3F','#581845']

# Get user input for rotations
rotations = askinteger('Enter Integer', 'Integer rotations: ')

# Convert the image to an RGBA format we can process, double sharpen it, and save that to an array
img = img.convert("RGBA")
datas = img.getdata() 

# Loop through array of the image and make all < blacks transparent
blacks = 0
newData = []
for item in datas:
    if item[0] <= blacks and item[1] <= blacks and item[2] <= blacks:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

# Convert RGB to hex
def rgb2hex(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex

# Loop through array of the image and make non colors transparent
# newData = []
# for item in datas:
#     if rgb2hex(item[0], item[1], item[2]) == colors[0] or colors[1] or colors[2] or colors[3] or colors[4]:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# Store the new processed array back to the img
img.putdata(newData)

# Take the new processed img, rotate and paste it over the original times times, and return that image
def rotate_and_paste(img, times):
    x = 360/times
    # Load original image, get size of it, and calculate the location of the paste
    background = Image.new('RGB', (new_w, new_h))
    bg_w, bg_h = background.size
    for i in range(0,times+1):
        # Rotate image x degrees
        img = img.rotate(x)
        # Get image size
        img_w, img_h = img.size
        # calculate the location of the paste
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        # paste the new rotated image over the original
        background.paste(img, offset, img)
    return background

background = rotate_and_paste(img, rotations)

# Get user input of where to save file
save_path = tk.filedialog.asksaveasfilename(initialfile = "RotatedWallpaper.png", 
                                            title = "Save New File As", defaultextension='.png',
                                            filetypes=[('PNG file','*.png')])

# Save the image to a new file
background.save(save_path)
