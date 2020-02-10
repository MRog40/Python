from PIL import Image
import tkinter as tk; from tkinter import filedialog
tk.Tk().withdraw()

# Get png filepath
file_path = tk.filedialog.askopenfilename()
picture = Image.open(file_path).convert('RGB')

# Get the size of the image
width, height = picture.size

# Process every pixel
for x in range(width):
   for y in range(height):
        r, g, b = picture.getpixel((x,y))
        new_color = r, g, b + 255
        picture.putpixel( (x,y), new_color)

# Get user input of where to save file
save_path = tk.filedialog.asksaveasfilename(initialfile = "BluePNG.png", 
                                            title = "Save New File As", defaultextension='.png',
                                            filetypes=[('PNG file','*.png')])

# Save the image to a new file
picture.save(save_path)
