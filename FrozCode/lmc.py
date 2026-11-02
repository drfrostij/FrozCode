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
    print("Create LMC Program button clicked")

def lmclanguageguidelete():
    print("Delete LMC Program button clicked")

def lmclanguageguiopen():
    print("Open LMC Program button clicked")

