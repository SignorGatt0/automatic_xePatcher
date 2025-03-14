import tkinter as tk
from tkinter.filedialog import askdirectory
import subprocess
import os
import shutil
from tkinter import ttk
# Create the main window
window = tk.Tk()
window.title("automatic_xePatcher")

# Set the window size
window.geometry("600x250")

# Change the background color using configure
window.configure(bg='grey')

input = None
output = None

def ask_what_directory_to_use_input():
    global input
    input = askdirectory(title='select a directory') # shows dialog box for asking the path to the user
    print(input)

def ask_what_directory_to_use_output():
    global output
    output = askdirectory(title='select a directory') # shows dialog box for asking the path to the user

def start_patching(): # the program starts to patching files
    """
    this function start to patch all the .xex file,
    'input' and 'output' are directory path.
    """

    if input != None and output != None:
        files = os.listdir(input)

        # move the input files to output folder
        for position in range(len(files)):
            file = files[position]
            if ".xex" in file: # check if the file is a .xex file
                shutil.move(f"{input}/{file}", output) # move (only the .xex file) that need to be patched in the output directrory
        files = os.listdir(output)

        # patch all the file
        for file in files:
            file_to_patch = str(file) #convert the type list to a string for the comand
            subprocess.run(f"XePatcher\XexTool.exe -m r -r a {file_to_patch}") # comand for patching a file
    elif input != None and output == None:
        files = os.listdir(input)

        for file in files:
            if ".xex" in file:
                file_to_patch = str(file) #convert the type list to a string for the comand
                subprocess.run(f"XePatcher\XexTool.exe -m r -r a {file_to_patch}") # comand for patching a file
    else:
        pass #TODO say to the user to select a directory

# getting the path to use
button1 = tk.Button(
                   command=ask_what_directory_to_use_input,
                   activebackground="white", 
                   activeforeground="white",
                   anchor="center",
                   bd=2,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 10),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=18,
                   pady=5,
                   width=30,
                   wraplength=100,
                   text="SELECT THE INPUT FOLDER")
button1.pack()

button2 = tk.Button(
                   command=ask_what_directory_to_use_output,
                   activebackground="white", 
                   activeforeground="white",
                   anchor="center",
                   bd=2,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 10),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=18,
                   pady=5,
                   width=30,
                   wraplength=100,
                   text="SELECT THE OUTPUT")
button2.pack()

button3 = tk.Button(
                   command=start_patching,
                   activebackground="white", 
                   activeforeground="white",
                   anchor="center",
                   bd=2,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="white",
                   fg="black",
                   font=("Arial", 10),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=18,
                   pady=5,
                   width=30,
                   wraplength=100,
                   text="START PATCHING")
button3.pack()

#creating the text on screen
lable1 = tk.Label(text = "If you don't select the output folder,\nthe file get all patched in the input folder without creating a copy of the .xex files", bg = "grey", fg = "white",relief = "groove")
lable1.pack()
window.mainloop()