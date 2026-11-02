###################################
#                                 #
#    Created By DrFrostij         #
#                                 #
###################################


########################
# The imports section  #
########################

from lmcvariables import run_program

import os                       # this is used to get the images + sounds we want                   # (needs pip installment)
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

def lmclanguageguicreate():
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new LMC program file which will be a text file that is just read when by a python function to run the LMC program
    print("Create LMC Program button clicked")
    global lmclanguageguicreateprogramname
    lmclanguageguicreateprogramname = customtkinter.CTk()
    lmclanguageguicreateprogramname.title("Create LMC Program")
    lmclanguageguicreateprogramname.geometry("400x300")
    entry = customtkinter.CTkEntry(lmclanguageguicreateprogramname, placeholder_text="CTkEntry")
    entry.pack(pady=20, padx=20)
    # Pop up a message box that says it was created successfully
    messagebox.showinfo("Create LMC Program", "LMC Program file created successfully!")

def lmclanguageguidelete():
    # This function deletes the text file that is the LMC program file that was created by the create function
    print("Delete LMC Program button clicked")
    # Pop up a message box that says it was deleted successfully
    messagebox.showinfo("Delete LMC Program", "LMC Program file deleted successfully!")

def lmclanguageguiopen():
    # This function opens the text file that is the LMC program file that was created by the create function
    print("Open LMC Program button clicked")
    # Pop up a message box that says it was opened successfully
    messagebox.showinfo("Open LMC Program", "LMC Program file opened successfully!")
