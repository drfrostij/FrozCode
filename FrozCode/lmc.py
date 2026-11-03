###################################
#                                 #
#    Created By DrFrostij         #
#                                 #
###################################


########################
# The imports section  #
########################

from lmcvariables import run_program

import os                       # this is used to get the files we want                             # (needs pip installment)
# https://docs.python.org/3/library/os.html                                                         #OS documentation
import pygame                   # this is for the graphics and sounds                               # (needs pip installment)
#https://www.pygame.org/docs/                                                                       #Pygame documentation
import customtkinter as customtkinter  # this is for the GUI                                        # (needs pip installment)
#https://customtkinter.tomschimansky.com                                                            #Custom Tkinter documentation
from PIL import Image, ImageTk          # this is for loading images                                # (needs pip installment)
#https://pillow.readthedocs.io/en/stable/                                                           #PIL documentation
from tkinter import HORIZONTAL, Button, Scale, mainloop, messagebox    #pop ups                     # (needs pip installment)
#https://docs.python.org/3/library/tkinter.messagebox.html                                          #Message box documentation    
import tkinter                                                                                      #PIL documentation
#https://docs.python.org/3/library/tkinter.html  

##########################
# Main Startup Code Area #
##########################


################################
# LMC Coding functions Section #
################################

program = '''
say "Hello from FrostLang!"
set score = 10
add score 5
say score
'''

run_program(program)

#############################
# LMC GUI Functions Section #
#############################


# Creates a new LMC program file which will be a text file that is just read when by a python function to run the LMC program




def createlmc(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new LMC program file which will be a text file that is just read when by a python function to run the LMC program
    print("Create LMC Program button clicked")
    # Pop up a message box that says it was created successfully
    messagebox.showinfo("Create LMC Program", "LMC Program file created successfully!")
    createlmcfile = entry.get()  # Get the value of the entry widget
    print(createlmcfile)

    # Create a new text file with the name of the entry widget
    with open(createlmcfile + ".txt", "a") as f:
       f.write("Welcome to FrostLang! This is your new LMC program file. You can start coding here.")

    # Put the new text file in a text file called "lmcprograms.txt" that is a list of all the LMC programs that have been created
    with open("lmcprograms.txt", "a") as f:
        f.write(createlmcfile + ".txt\n")

    # Close the GUI window
    lmclanguageguicreateprogramname.destroy()





def lmclanguageguicreate():
    global lmclanguageguicreateprogramname
    lmclanguageguicreateprogramname = customtkinter.CTk()
    lmclanguageguicreateprogramname.title("Create LMC Program")
    lmclanguageguicreateprogramname.geometry("300x200")
    entry = customtkinter.CTkEntry(lmclanguageguicreateprogramname, placeholder_text="Enter LMC Name")
    entry.grid(row=1, column=0, pady=20, padx=20)
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createlmcfile = customtkinter.CTkButton(lmclanguageguicreateprogramname, text="Create LMC Program", command=lambda:createlmc(entry))
    createlmcfile.grid(row=2, column=0, padx=20, pady=20)
    lmclanguageguicreateprogramname.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    lmclanguageguicreateprogramname.mainloop()













# Deletes the text file that is the LMC program file that was created by the create function

def lmclanguageguidelete():
    # This function deletes the text file that is the LMC program file that was created by the create function
    print("Delete LMC Program button clicked")
    # Pop up a message box that says it was deleted successfully
    messagebox.showinfo("Delete LMC Program", "LMC Program file deleted successfully!")






# Opens the text file that is the LMC program file that was created by the create function

def lmclanguageguiopen():
    # This function opens the text file that is the LMC program file that was created by the create function
    print("Open LMC Program button clicked")
    # Pop up a message box that says it was opened successfully
    messagebox.showinfo("Open LMC Program", "LMC Program file opened successfully!")
