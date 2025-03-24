import tkinter as tk
from tkinter.filedialog import askdirectory
import subprocess
import os
import shutil
from tkinter import ttk
from threading import Thread
# Create the main window
window = tk.Tk()
window.title("automatic_xePatcher")

# Set the window size
window.geometry("720x480")

# Change the background color using configure
window.configure(bg='grey')

input_ = None
output = None

def ask_what_directory_to_use_input():
    global input_
    input_ = askdirectory(title='select a directory') # shows dialog box for asking the path to the user
    lable2 = tk.Label(text = input_, bg = "white", fg = "black",relief = "groove",width=80)
    lable2.place(relx = 4.0, 
                  rely = 0.0,
                  anchor ='ne')
    lable2.pack()

def ask_what_directory_to_use_output():
    global output
    output = askdirectory(title='select a directory') # shows dialog box for asking the path to the user

def show_founded_xex():
    pass

def show_selected_input():
    pass

def show_selected_output():
    pass

def start_patching(): # the program starts to patching files
    """
    this function start to patch all the .xex file,
    'input_' and 'output' are directory path.
    """
    
    if input_ != None and output != None:
        files = os.listdir(input_)
        xex_files_found = []

        for file in files:
            if ".xex" in file:

                xex_files_found.append(file)

                file_to_patch = str(file) #convert the type list to a string for the comand
                subprocess.run(f"XePatcher\XexTool.exe -m r -r a \"{file_to_patch}\"") # comand for patching a file

            if len(xex_files_found) == 0:
                raise ValueError("NO .xex files found")
        # move the input_ files to output folder
        for position in range(len(files)):
            file = files[position]
            if ".xex" in file: # check if the file is a .xex file
                shutil.move(f"{input_}/{file}", output) # move (only the .xex file) that need to be patched in the output directrory

        files = os.listdir(output)

        # patch all the file
        for file in files:
            file_to_patch = str(file) #convert the type list to a string for the comand
            subprocess.run(f"XePatcher\XexTool.exe -m r -r a {file_to_patch}") # comand for patching a file

    elif input_ != None and output == None:
        all_files = os.listdir(input_)
        last_foulder = input_
        search_and_patch(all_files,last_foulder)
    else:
        pass #TODO say to the user to select a directory

def search_and_patch(all_files,last_foulder):
    threads = []
    for file in all_files:
        t = Thread(target=for_threading, args=(file,last_foulder))
        t.start()
        threads.append(t)

    # Wait all threads to finish.
    for t in threads:
        t.join()
        
def for_threading(file,last_foulder):
    if ".xex" in file: # file to patch found
            file_to_patch = str(f"{last_foulder}/{file}") #convert the type list to a string for the comand
            subprocess.run(f"XePatcher\XexTool.exe -m r -r a \"{file_to_patch}\"") # comand for patching a file

    elif not "." in file: # directory found
        new_all_file = os.listdir(f"{last_foulder}/{file}")
        for file_ in new_all_file:
            if ".xex" in file_: # file to patch found
                file_to_patch_ = str(f"{last_foulder}/{file}/{file_}") #convert the type list to a string for the command
                subprocess.run(f"XePatcher\XexTool.exe -m r -r a \"{file_to_patch_}\"") # comand for patching a file
            else:
                pass

# getting the path to use
button1 = tk.Button(
                   command=ask_what_directory_to_use_input,
                   activebackground="white", 
                   activeforeground="white",
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
                   overrelief="raised",
                   padx=18,
                   pady=5,
                   width=10,
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
                   width=10,
                   wraplength=100,
                   text="SELECT THE OUTPUT")
button2.pack()

button3 = tk.Button(
                   command=start_patching,
                   activebackground="grey", 
                   activeforeground="grey",
                   anchor="center",
                   bd=2,
                   bg="black",
                   cursor="hand2",
                   disabledforeground="grey",
                   fg="white",
                   font=("Arial", 10),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=20,
                   pady=5,
                   width=5,
                   wraplength=100,
                   text="START PATCHING")
button3.pack()


#creating the text on screen

lable1 = tk.Label(text = "If you don't select the output folder,\nthe file get all patched in the input folder without creating a copy of the .xex files", bg = "grey", fg = "white",relief = "groove")
lable1.pack()
window.mainloop()
