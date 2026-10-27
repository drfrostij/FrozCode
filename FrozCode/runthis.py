###################################
#                                 #
#    Created By DrFrostij         #
#                                 #
###################################


########################
# The imports section  #
########################


from FrozCodeMain import run_program


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

program = '''
say "Hello from FrostLang!"
set score = 10
add score 5
say score
'''

run_program(program)


def mainGUI():
    global mainpage
    mainpage = customtkinter.CTk()
    mainpage.title("FrostLang GUI")
    mainpage.geometry("400x300")
    # Logo
    logo = customtkinter.CTkButton(mainpage, text="Select language")
    logo.grid(row=0, column=0, padx=20, pady=20)
    logo.configure(state="enabled")
    logo.configure(fg_color="light blue")
    logo.configure(width=200, height=50)
    logo.configure(font=("Arial", 30))
    logo.configure(text_color="Black")
    # Choose language button area
    # LMC langauge
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    lmc = customtkinter.CTkButton(mainpage, text="Little Man Computing / LMC", command=lambda:lmclanguagegui())
    lmc.grid(row=1, column=0, padx=20, pady=20)
    mainpage.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    python = customtkinter.CTkButton(mainpage, text="Python", command=lambda:pythonlanguagegui())
    python.grid(row=2, column=0, padx=20, pady=20)
    mainpage.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    java = customtkinter.CTkButton(mainpage, text="Java (Not Implemented Yet)", command=lambda:javalanguagegui())
    java.grid(row=3, column=0, padx=20, pady=20)
    mainpage.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    mainpage.mainloop()


def lmclanguagegui():
    print("LMC language GUI")

def pythonlanguagegui():
    print("Python language GUI")

def javalanguagegui():
    print("Java language GUI")

#
# Start the main GUI
#

mainGUI()