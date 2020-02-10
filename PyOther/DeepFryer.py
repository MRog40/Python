# Michael Rogers
from PIL import Image, ImageEnhance
import tkinter as tk; from tkinter import filedialog
tk.Tk().withdraw()
file_path = tk.filedialog.askopenfilename()
img = ImageEnhance.Color(Image.open(file_path)).enhance(9)
img.save((file_path[:-4]+"FRIED.jpg").replace('/', '\\'), quality=2)
