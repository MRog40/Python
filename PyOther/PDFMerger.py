import tkinter as tk; from tkinter import filedialog
from PyPDF2 import PdfFileMerger, PdfFileReader

tk.Tk().withdraw()

filename1 = tk.filedialog.askopenfilename(title = "Select First PDF")
filename2 = tk.filedialog.askopenfilename(title = "Select Second PDF")

merger = PdfFileMerger()

merger.append(PdfFileReader(open(filename1, 'rb')))
merger.append(PdfFileReader(open(filename2, 'rb')))

save_path = tk.filedialog.asksaveasfilename(initialfile = "Merged.pdf",
                                            title = "Save PDF As", defaultextension='.pdf',
                                            filetypes=[('PDF file','*.pdf')])

merger.write(save_path)