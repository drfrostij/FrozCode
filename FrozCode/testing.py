
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


openlmcfile="frostlang/testlmc.txt"  # this is the name of the file we want to open, it can be changed to any other file name

print("Opening LMC Program file: " + openlmcfile)
# Open the text file with the name of the entry widget
global lmcfileviewerwindowet
lmcfileviewerwindowet = customtkinter.CTk()
lmcfileviewerwindowet.title("LMC Program Viewer")
lmcfileviewerwindowet.geometry("800x600")
text_widget = customtkinter.CTkTextbox(lmcfileviewerwindowet)
text_widget.pack(fill="both", expand=True)
with open("frostlang/" + openlmcfile, "r") as f:
    text_widget.insert("1.0", f.read())
lmcfileviewerwindowet.mainloop()
