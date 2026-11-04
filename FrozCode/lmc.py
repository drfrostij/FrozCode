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

######################################################
#                                                    #
#               MAIN LMC GUI EDITOR                  #
#                                                    #
######################################################


def lmcfileviewer(openlmcfile):
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

    


##################################################################################################################################
# Creates a new LMC program file which will be a text file that is just read when by a python function to run the LMC program    #
##################################################################################################################################


# The god of creation functions

def createlmc(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new LMC program file which will be a text file that is just read when by a python function to run the LMC program
    print("Create LMC Program button clicked")
    # Pop up a message box that says it was created successfully
    createlmcfile = entry.get()  # Get the value of the entry widget
    print(createlmcfile + "lmc.txt")


    # Create a new text file with the name of the entry widget
    with open("frostlang/" + createlmcfile + "lmc.txt", "a") as f:
       f.write("Welcome to FrostLang! This is your new LMC program file. You can start coding here.")

    # Put the new text file in a text file called "lmcprograms.txt" that is a list of all the LMC programs that have been created

    createlmcfile = createlmcfile + "lmc.txt"  # Add the .txt extension to the file name


    with open("lmcprograms.txt", "a") as f:
        f.write(createlmcfile + "lmc.txt\n")

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
    messagebox.showinfo("Create LMC Program", "LMC Program file creater has opened successfully! Please enter the name of your new LMC program file and click the Create LMC Program button to create it.")

    lmclanguageguicreateprogramname.mainloop()

#################################################################################################
# Deletes the text file that is the LMC program file that was created by the create function    #
#################################################################################################

def deletelmc(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new LMC program file which will be a text file that is just read when by a python function to run the LMC program
    print("Delete LMC Program button clicked")
    # Pop up a message box that says it was deleted successfully
    deletelmcfile = entry.get()  # Get the value of the entry widget
    print(deletelmcfile + "lmc.txt")

    # Delete the text file with the name of the entry widget
    if os.path.exists("frostlang/" + deletelmcfile + "lmc.txt"):
      os.remove("frostlang/" + deletelmcfile + "lmc.txt")
      messagebox.showinfo("Delete LMC Program", "LMC Program file deleted successfully!")
    else:
        messagebox.showinfo("Delete LMC Program", "LMC Program file does not exist or could not be deleted!")

    # Remove the deleted text file from the "lmcprograms.txt" list of all the LMC programs that have been created

    deletelmcfile = deletelmcfile + "lmc.txt"  # Add the .txt extension to the file name

    with open("lmcprograms.txt", "r") as f:
        lines = f.readlines()                           # Read all lines from the file
    with open("lmcprograms.txt", "w") as f:
        for line in lines:
            if line.strip() != deletelmcfile:           # If the line does not match the deleted file name, write it back to the file
                f.write(line)

    # Close the GUI window
    lmclanguageguideleteprogramname.destroy()

def lmclanguageguidelete():
    global lmclanguageguideleteprogramname
    lmclanguageguideleteprogramname = customtkinter.CTk()
    lmclanguageguideleteprogramname.title("Delete LMC Program")
    lmclanguageguideleteprogramname.geometry("300x200")
    entry = customtkinter.CTkEntry(lmclanguageguideleteprogramname, placeholder_text="Enter LMC Name")
    entry.grid(row=1, column=0, pady=20, padx=20)
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createlmcfile = customtkinter.CTkButton(lmclanguageguideleteprogramname, text="Delete LMC Program", command=lambda:deletelmc(entry))
    createlmcfile.grid(row=2, column=0, padx=20, pady=20)
    lmclanguageguideleteprogramname.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    messagebox.showinfo("Delete LMC Program", "LMC Program file deleter has opened successfully! Please enter the name of your LMC program file and click the Delete LMC Program button to delete it.")

    lmclanguageguideleteprogramname.mainloop()

##################################################################################################
# Opens the text file that is the LMC program file that was created by the create function       #
##################################################################################################

def openlmc(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new LMC program file which will be a text file that is just read when by a python function to run the LMC program
    print("Open LMC Program button clicked")
    # Pop up a message box that says it was opened successfully
    openlmcfile = entry.get()  # Get the value of the entry widget
    print(openlmcfile)

    # Delete the text file with the name of the entry widget
    if os.path.exists("frostlang/" + openlmcfile + "lmc.txt"):
      os.remove("frostlang/" + openlmcfile + "lmc.txt")
      messagebox.showinfo("Open LMC Program", "LMC Program file opened successfully!")
      lmcfileviewer(openlmcfile + "lmc.txt")
    else:
        messagebox.showinfo("Open LMC Program", "LMC Program file does not exist or could not be opened!")

    # Close the GUI window
    lmclanguageguiopenprogramname.destroy()

def lmclanguageguiopen():
    global lmclanguageguiopenprogramname
    lmclanguageguiopenprogramname = customtkinter.CTk()
    lmclanguageguiopenprogramname.title("Open LMC Program")
    lmclanguageguiopenprogramname.geometry("300x200")
    entry = customtkinter.CTkEntry(lmclanguageguiopenprogramname, placeholder_text="Enter LMC Name")
    entry.grid(row=1, column=0, pady=20, padx=20)
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createlmcfile = customtkinter.CTkButton(lmclanguageguiopenprogramname, text="Open LMC Program", command=lambda:openlmc(entry))
    createlmcfile.grid(row=2, column=0, padx=20, pady=20)
    lmclanguageguiopenprogramname.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    messagebox.showinfo("Open LMC Program", "LMC Program file opener has opened successfully! Please enter the name of your LMC program file and click the Open LMC Program button to open it.")

    lmclanguageguiopenprogramname.mainloop()
