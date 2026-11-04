###################################
#                                 #
#    Created By DrFrostij         #
#                                 #
###################################

########################
# The imports section  #
########################


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

##############################
# Java GUI Functions Section #
##############################



######################################################
#                                                    #
#               MAIN JAVA GUI EDITOR                 #
#                                                    #
######################################################

def javafileviewer(javafile):
    # This function opens the Java program file in a new window and displays the contents of the file in a text widget
    javafileviewer = customtkinter.CTk()
    javafileviewer.title("Java Program Viewer")
    javafileviewer.geometry("600x400")
    text_widget = customtkinter.CTkTextbox(javafileviewer)
    text_widget.pack(fill="both", expand=True)
    with open("frostlang/" + javafile, "r") as f:
        text_widget.insert("1.0", f.read())
    javafileviewer.mainloop()




# The god of creation functions
# This is basically the same as the LMC GUI functions section, but for Java programs instead of LMC programs. The functions are the same, but they are for Java programs instead of LMC programs.


####################################################################################################################################
# Creates a new Java program file which will be a text file that is just read when by a python function to run the Java program    #
####################################################################################################################################


# The god of creation functions

def createjava(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new Java program file which will be a text file that is just read when by a python function to run the Java program
    print("Create Java Program button clicked")
    # Pop up a message box that says it was created successfully
    createjavafile = entry.get()  # Get the value of the entry widget
    print(createjavafile + "java.txt")


    # Create a new text file with the name of the entry widget
    with open("frostlang/" + createjavafile + "java.txt", "a") as f:
       f.write("Welcome to FrostLang! This is your new Java program file. You can start coding here.")

    # Put the new text file in a text file called "javaprograms.txt" that is a list of all the Java programs that have been created

    createjavafile = createjavafile + "java.txt"  # Add the .txt extension to the file name


    with open("javaprograms.txt", "a") as f:
        f.write(createjavafile + "java.txt\n")

    # Close the GUI window
    javalanguageguicreateprogramname.destroy()

def javalanguageguicreate():
    global javalanguageguicreateprogramname
    javalanguageguicreateprogramname = customtkinter.CTk()
    javalanguageguicreateprogramname.title("Create Java Program")
    javalanguageguicreateprogramname.geometry("300x200")
    entry = customtkinter.CTkEntry(javalanguageguicreateprogramname, placeholder_text="Enter Java Name")
    entry.grid(row=1, column=0, pady=20, padx=20)
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createjavafile = customtkinter.CTkButton(javalanguageguicreateprogramname, text="Create Java Program", command=lambda:createjava(entry))
    createjavafile.grid(row=2, column=0, padx=20, pady=20)
    javalanguageguicreateprogramname.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    messagebox.showinfo("Create Java Program", "Java Program file created has opened successfully! Please enter the name of your new Java program file and click the Create Java Program button to create it.")

    javalanguageguicreateprogramname.mainloop()

##################################################################################################
# Deletes the text file that is the Java program file that was created by the create function    #
##################################################################################################

def deletejava(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new Java program file which will be a text file that is just read when by a python function to run the Java program
    print("Delete Java Program button clicked")
    # Pop up a message box that says it was deleted successfully
    deletejavafile = entry.get()  # Get the value of the entry widget
    print(deletejavafile + "java.txt")

    # Delete the text file with the name of the entry widget
    if os.path.exists("frostlang/" + deletejavafile + "java.txt"):
      os.remove("frostlang/" + deletejavafile + "java.txt")
      messagebox.showinfo("Delete Java Program", "Java Program file deleted successfully!")
    else:
        messagebox.showinfo("Delete Java Program", "Java Program file does not exist or could not be deleted!")

    # Remove the deleted text file from the "javaprograms.txt" list of all the Java programs that have been created

    deletejavafile = deletejavafile + "java.txt"  # Add the .txt extension to the file name

    with open("javaprograms.txt", "r") as f:
        lines = f.readlines()                           # Read all lines from the file
    with open("javaprograms.txt", "w") as f:
        for line in lines:
            if line.strip() != deletejavafile:           # If the line does not match the deleted file name, write it back to the file
                f.write(line)

    # Close the GUI window
    javalanguageguideleteprogramname.destroy()

def javalanguageguidelete():
    global javalanguageguideleteprogramname
    javalanguageguideleteprogramname = customtkinter.CTk()
    javalanguageguideleteprogramname.title("Delete Java Program")
    javalanguageguideleteprogramname.geometry("300x200")
    entry = customtkinter.CTkEntry(javalanguageguideleteprogramname, placeholder_text="Enter Java Program Name")
    entry.grid(row=1, column=0, pady=20, padx=20)
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createjavafile = customtkinter.CTkButton(javalanguageguideleteprogramname, text="Delete Java Program", command=lambda:deletejava(entry))
    createjavafile.grid(row=2, column=0, padx=20, pady=20)
    javalanguageguideleteprogramname.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    messagebox.showinfo("Delete Java Program", "Java Program file deleter has opened successfully! Please enter the name of your Java program file and click the Delete Java Program button to delete it.")

    javalanguageguideleteprogramname.mainloop()

###################################################################################################
# Opens the text file that is the Java program file that was created by the create function       #
###################################################################################################

def openjava(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new Java program file which will be a text file that is just read when by a python function to run the Java program
    print("Open Java Program button clicked")
    # Pop up a message box that says it was opened successfully
    openjavafile = entry.get()  # Get the value of the entry widget
    print(openjavafile)

    # Delete the text file with the name of the entry widget
    if os.path.exists("frostlang/" + openjavafile + "java.txt"):
      os.remove("frostlang/" + openjavafile + "java.txt")
      messagebox.showinfo("Open Java Program", "Java Program file opened successfully!")
      javafileviewer(openjavafile + "java.txt")
    else:
        messagebox.showinfo("Open Java Program", "Java Program file does not exist or could not be opened!")

    # Close the GUI window
    javalanguageguiopenprogramname.destroy()

def javalanguageguiopen():
    global javalanguageguiopenprogramname
    javalanguageguiopenprogramname = customtkinter.CTk()
    javalanguageguiopenprogramname.title("Open Java Program")
    javalanguageguiopenprogramname.geometry("300x200")
    entry = customtkinter.CTkEntry(javalanguageguiopenprogramname, placeholder_text="Enter Java Program Name")
    entry.grid(row=1, column=0, pady=20, padx=20)
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createjavafile = customtkinter.CTkButton(javalanguageguiopenprogramname, text="Open Java Program", command=lambda:openjava(entry))
    createjavafile.grid(row=2, column=0, padx=20, pady=20)
    javalanguageguiopenprogramname.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    messagebox.showinfo("Open Java Program", "Java Program file opener has opened successfully! Please enter the name of your Java program file and click the Open Java Program button to open it.")

    javalanguageguiopenprogramname.mainloop()
