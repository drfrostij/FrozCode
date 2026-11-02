###################################
#                                 #
#    Created By DrFrostij         #
#                                 #
###################################


########################
# The imports section  #
########################

from lmc import lmclanguageguicreate, lmclanguageguidelete, lmclanguageguiopen
from python import pythonlanguageguicreate, pythonlanguageguidelete, pythonlanguageguiopen
from java import javalanguageguicreate, javalanguageguidelete, javalanguageguiopen

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
    global lmcgui
    lmcgui = customtkinter.CTk()
    lmcgui.title("LMC GUI")
    lmcgui.geometry("400x300")
    # Logo
    lmclogo = customtkinter.CTkButton(lmcgui, text="Select the options of LMC")
    lmclogo.grid(row=0, column=0, padx=20, pady=20)
    lmclogo.configure(state="enabled")
    lmclogo.configure(fg_color="light blue")
    lmclogo.configure(width=200, height=50)
    lmclogo.configure(font=("Arial", 30))
    lmclogo.configure(text_color="Black")
    # Choose language button area
    # LMC langauge
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createlmc = customtkinter.CTkButton(lmcgui, text="Create LMC Program", command=lambda:lmclanguageguicreate())
    createlmc.grid(row=1, column=0, padx=20, pady=20)
    lmcgui.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    deletemlc = customtkinter.CTkButton(lmcgui, text="Delete LMC Program", command=lambda:lmclanguageguidelete())
    deletemlc.grid(row=2, column=0, padx=20, pady=20)
    lmcgui.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    openlmc = customtkinter.CTkButton(lmcgui, text="Open LMC Program", command=lambda:lmclanguageguiopen())
    openlmc.grid(row=3, column=0, padx=20, pady=20)
    lmcgui.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    lmcgui.mainloop()

def pythonlanguagegui():
    global pythongui
    pythongui = customtkinter.CTk()
    pythongui.title("Python GUI")
    pythongui.geometry("400x300")
    # Logo
    pylogo = customtkinter.CTkButton(pythongui, text="Select the options of Python")
    pylogo.grid(row=0, column=0, padx=20, pady=20)
    pylogo.configure(state="enabled")
    pylogo.configure(fg_color="light blue")
    pylogo.configure(width=200, height=50)
    pylogo.configure(font=("Arial", 30))
    pylogo.configure(text_color="Black")
    # Choose language button area
    # LMC langauge
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createpython = customtkinter.CTkButton(pythongui, text="Create Python Program", command=lambda:pythonlanguageguicreate())
    createpython.grid(row=1, column=0, padx=20, pady=20)
    pythongui.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    deletepython = customtkinter.CTkButton(pythongui, text="Delete Python Program", command=lambda:pythonlanguageguidelete())
    deletepython.grid(row=2, column=0, padx=20, pady=20)
    pythongui.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    openpython = customtkinter.CTkButton(pythongui, text="Open Python Program", command=lambda:pythonlanguageguiopen())
    openpython.grid(row=3, column=0, padx=20, pady=20)
    pythongui.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    pythongui.mainloop()

def javalanguagegui():
    global javagui
    javagui = customtkinter.CTk()
    javagui.title("Java GUI")
    javagui.geometry("400x300")
    # Logo
    javalogo = customtkinter.CTkButton(javagui, text="Select the options of Java")
    javalogo.grid(row=0, column=0, padx=20, pady=20)
    javalogo.configure(state="enabled")
    javalogo.configure(fg_color="light blue")
    javalogo.configure(width=200, height=50)
    javalogo.configure(font=("Arial", 30))
    javalogo.configure(text_color="Black")
    # Choose language button area
    # LMC langauge
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createjava = customtkinter.CTkButton(javagui, text="Create Java Program", command=lambda:javalanguageguicreate())
    createjava.grid(row=1, column=0, padx=20, pady=20)
    javagui.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    deletejava = customtkinter.CTkButton(javagui, text="Delete Java Program", command=lambda:javalanguageguidelete())
    deletejava.grid(row=2, column=0, padx=20, pady=20)
    javagui.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    openjava = customtkinter.CTkButton(javagui, text="Open Java Program", command=lambda:javalanguageguiopen())
    openjava.grid(row=3, column=0, padx=20, pady=20)
    javagui.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    javagui.mainloop()

#
# Start the main GUI
#

mainGUI()