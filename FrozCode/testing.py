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




global lmclanguageguicreateprogramname
lmclanguageguicreateprogramname = customtkinter.CTk()
lmclanguageguicreateprogramname.title("Create LMC Program")
lmclanguageguicreateprogramname.geometry("400x300")
entry = customtkinter.CTkEntry(lmclanguageguicreateprogramname, placeholder_text="CTkEntry")
entry.pack(pady=20, padx=20)


lmclanguageguicreateprogramname.mainloop()