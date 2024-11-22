import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk


root = tk.Tk()
root.title("Tkinter Open File Dialog")
root.resizable(width=False, height=False)
root.geometry("300x150")


def select_file():
    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )

    mb.showinfo(
        title='Selected File',
        message=filename
    )

    open_file(filename)
    print("This Analysis Report is of", filename, '\n\n')


open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


def open_file(filename):
    import cfgAutograder
    cfgAutograder.analyse_code(cfgAutograder.code_conversion(filename))


root.mainloop()

