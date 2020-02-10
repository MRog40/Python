from PIL import Image
import os
import tkinter as tk; from tkinter import filedialog; from tkinter import messagebox
from tkinter.simpledialog import askstring, askinteger

# Get file directory
tk.Tk().withdraw()
folder_path = tk.filedialog.askdirectory()
directory = os.fsencode(folder_path)

counter = 0

def bmp2jpg(bmp_file):
	jpg_file = bmp_file[0:len(bmp_file)-3] + "jpg"
	img = Image.open(bmp_file)
	img.save(jpg_file, "JPEG", quality=100, optimize=True, progressive=True)
	os.remove(bmp_file)

# Loop through folder and convert each image
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".bmp"):
		bmp2jpg(os.fsdecode(os.path.join(directory, file)))
		counter += 1
		continue
	else:
		continue

messagebox.showinfo("MR bmp2jpg", "Converted " + str(counter) + " BMPs to JPGs")