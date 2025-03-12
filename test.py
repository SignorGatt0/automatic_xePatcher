#import tkinter as tk
import subprocess
import os
import shutil

# window = tk.Tk()
# window.title("AUTOMATIC_XEPATCHER")


def start_patching(): # the program starts to patching files
    """
    this function start to patch all the .xex file from the "input" directory
    """
    files = os.listdir("input")
    try:
        os.mkdir("output") # create the output directory
    except:
        pass

    for position in range(len(files)):
        file = files[position]
        if ".xex" in file: # check if the file in the directory "input"(TODO custom directory) is a .xex file
            shutil.move(f"input/{file}", "output/") # move (only the .xex file) that need to be patched in the output directrory

    files = os.listdir("output")
    for file in files:
        file_to_patch = str(file) #convert the type list to a string for the comand
        subprocess.run(f"XePatcher\XexTool.exe -m r -r a {file_to_patch}") # comand for patching a file

start_patching()

# button = tk.Button(text="START PATCHING")
# button.bind("test", start_patching)
# button.pack()

# Start the event loop.
# window.mainloop()