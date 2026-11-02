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

##############################
# Java GUI Functions Section #
##############################

def javalanguageguicreate():
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new Java program file which will be a text file that is just read when by a python function to run the Java program
    print("Create Java Program button clicked")
    # Pop up a message box that says it was created successfully
    messagebox.showinfo("Create Java Program", "Java Program file created successfully!")

def javalanguageguidelete():
    # This function deletes the text file that is the Java program file that was created by the create function
    print("Delete Java Program button clicked")
    # Pop up a message box that says it was deleted successfully
    messagebox.showinfo("Delete Java Program", "Java Program file deleted successfully!")

def javalanguageguiopen():
    # This function opens the text file that is the Java program file that was created by the create function
    print("Open Java Program button clicked")
    # Pop up a message box that says it was opened successfully
    messagebox.showinfo("Open Java Program", "Java Program file opened successfully!")