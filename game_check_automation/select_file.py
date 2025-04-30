import tkinter as tk
from tkinter import filedialog


def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_selected = filedialog.askopenfilename(title="Select Excel File with IDs", filetypes=[("Excel files", "*.xlsx *.xls")])
    root.destroy()
    return file_selected
