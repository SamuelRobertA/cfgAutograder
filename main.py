# imports the tkinter library for GUI and imports the cfgAutograder file
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import cfgAutograder as cfg

# main window of the GUI
root = tk.Tk()
# Title of the GUI
root.title("CFG Autograder")
# Makes so that we can resize the window
root.resizable(width=True, height=True)
# adds a frame to the root
frame = ttk.Frame(root, padding=10)
# grid frame
frame.grid()
# to add the text widget to display the output in the window
text_widget = tk.Text(root, height=30, width=100)
# sets the position on the grid frame
text_widget.grid(column=0, row=3, padx=20, pady=20)

# Add a label to display the project name and team members
project_info = """CFG Autograder Project
Group Name : Logic Labs
Team Members:
1. Md Sabab Ur Rahman
2. Samuel Robert Antony Flay
3. Vishmi Kumara
4. Clelya Foumo
"""
info_label = ttk.Label(root, text=project_info, justify="center", font=("Arial", 12))
# Position the label at the top of the GUI
info_label.grid(column=0, row=0, padx=10, pady=10)

# opens the dialog to open a file from the computer
def select_file():
    # types of accepted file
    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )

    # file opening window settings
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )

    # dialog shows name of the selected file
    mb.showinfo(
        title='Selected File',
        message=filename
    )

    # calls the open_file function with the file name
    open_file(filename)

    # calls the function to display the output in the text widget
    display_output("This Analysis Report is of " + filename + '\n\n' + cfg.report())


# adds a button to the window to open the text file
open_button = ttk.Button(
    root,
    text='Open a File',
    # runs the select_file Function
    command=select_file
)

# Make the button larger and position it lower
open_button.config(width=20, padding=(10, 5))
# sets the position on the grid frame, with more padding
open_button.grid(column=0, row=1, padx=10, pady=20)


# opens the file and calls the analyse code and code conversion from cfgAutograder file
def open_file(filename):
    cfg.analyse_code(cfg.code_conversion(filename))


# displays the output in the text field
def display_output(output_text):
    # clears if there was a previous output
    text_widget.delete(1.0, tk.END)
    # adds the output
    text_widget.insert(tk.END, output_text)


# runs the primary window
root.mainloop()
