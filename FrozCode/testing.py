import os                       # this is used to get the files we want                             # (needs pip installment)
# https://docs.python.org/3/library/os.html                                                         #OS documentation
import customtkinter as customtkinter  # this is for the GUI                                        # (needs pip installment)
#https://customtkinter.tomschimansky.com                                                            #Custom Tkinter documentation
from tkinter import HORIZONTAL, Button, Scale, mainloop, messagebox    #pop ups                     # (needs pip installment)
#https://docs.python.org/3/library/tkinter.messagebox.html                                          #Message box documentation    
import tkinter                                                                                      # (needs pip installment)
#https://docs.python.org/3/library/tkinter.html                                                     #Tkinter documentation
from pathlib import Path                                                                            # (needs pip installment)



openlmcfile = "testlmc.txt"  # this is the name of the file we want to open, it can be changed to any other file name


def lmcfileviewer(openlmcfile):
    print("Opening LMC Program file: " + openlmcfile)

    # This opens the text file with the name of the entry widget in a new window and lets user edit it

    openlmcfile="testlmc.txt"  # this is the name of the file we want to open, it can be changed to any other file name
    print("Opening LMC Program file: " + openlmcfile)
    # Open the text file with the name of the entry widget
    global lmcfileviewerwindowet
    lmcfileviewerwindowet = customtkinter.CTk()
    lmcfileviewerwindowet.title("LMC Program Viewer")
    lmcfileviewerwindowet.geometry("800x600")
    text_widget = customtkinter.CTkTextbox(lmcfileviewerwindowet)
    text_widget.pack(fill="both", expand=True)
    BASE_DIR = Path(__file__).resolve().parent
    with open(BASE_DIR / "frostlang" / openlmcfile, "r") as f:
        text_widget.insert("1.0", f.read())


    # This is the save button that saves the text file with the name of the entry widget
    save_button = customtkinter.CTkButton(lmcfileviewerwindowet, text="Save", command=lambda: save_lmc_file(openlmcfile, text_widget))
    save_button.pack(pady=10)

    # This is the run button that runs the LMC program in the text file with the name of the entry widget
    run_button = customtkinter.CTkButton(lmcfileviewerwindowet, text="Run", command=lambda: run_program(text_widget.get("1.0", "end-1c")))
    run_button.pack(pady=10)


    lmcfileviewerwindowet.mainloop()


def save_lmc_file(openlmcfile, text_widget):
    # This function saves the text file with the name of the entry widget
    BASE_DIR = Path(__file__).resolve().parent
    with open(BASE_DIR / "frostlang" / openlmcfile, "w") as f:
        f.write(text_widget.get("1.0", "end-1c"))
    messagebox.showinfo("Save LMC Program", "LMC Program file saved successfully!")    

def run_program(program):
    # This function runs the LMC program in the text file with the name of the entry widget
    print("Running LMC Program...")
    # Here we will run the LMC program using the run_program function from lmcvariables.py
    # We will also display a message box that says it was run successfully
    messagebox.showinfo("Run LMC Program", "LMC Program ran successfully!")



lmcfileviewer(openlmcfile)  # this is the name of the file we want to open, it can be changed to any other file name