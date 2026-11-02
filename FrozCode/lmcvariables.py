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

variables = {}

def run_program(code):
    for line_number, line in enumerate(code.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        parts = line.split(" ", 2)
        command = parts[0]
        if command == "say":
            text = line[4:].strip()
            if text.startswith('"') and text.endswith('"'):
                text = text[1:-1]
            if text in variables:
                print(variables[text])
            else:
                print(text)
        elif command == "set":
            name = parts[1]
            value = parts[2]
            if value.isdigit():
                value = int(value)
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            variables[name] = value
        elif command == "add":
            name = parts[1]
            amount = int(parts[2])
            variables[name] = str(variables[name]) + str(amount)
        else:
            raise SyntaxError(
                f"Unknown command on line {line_number}: {command}"
            )
