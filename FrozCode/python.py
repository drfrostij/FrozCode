###################################
#                                 #
#    Created By DrFrostij         #
#                                 #
###################################


########################
# The imports section  #
########################

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
# Python GUI Functions Section #
################################

def pythonlanguageguicreate():
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new Python program file which will be a text file that is just read when by a python function to run the Python program
    print("Create Python Program button clicked")
    # Pop up a message box that says it was created successfully
    messagebox.showinfo("Create Python Program", "Python Program file created successfully!")

def pythonlanguageguidelete():
    # This function deletes the text file that is the Python program file that was created by the create function
    print("Delete Python Program button clicked")
    # Pop up a message box that says it was deleted successfully
    messagebox.showinfo("Delete Python Program", "Python Program file deleted successfully!")

def pythonlanguageguiopen():
    # This function opens the text file that is the Python program file that was created by the create function
    print("Open Python Program button clicked")
    # Pop up a message box that says it was opened successfully
    messagebox.showinfo("Open Python Program", "Python Program file opened successfully!")
