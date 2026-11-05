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
import customtkinter as customtkinter  # this is for the GUI                                        # (needs pip installment)
#https://customtkinter.tomschimansky.com                                                            #Custom Tkinter documentation
from tkinter import HORIZONTAL, Button, Scale, mainloop, messagebox    #pop ups                     # (needs pip installment)
#https://docs.python.org/3/library/tkinter.messagebox.html                                          #Message box documentation    
import tkinter                                                                                      # (needs pip installment)
#https://docs.python.org/3/library/tkinter.html                                                     #Tkinter documentation
from pathlib import Path                                                                            # (needs pip installment)

##########################
# Main Startup Code Area #
##########################

################################
# Python GUI Functions Section #
################################


######################################################
#                                                    #
#               MAIN PYTHON GUI EDITOR               #
#                                                    #
######################################################

def pythonfileviewer(filename):
    print("Python file viewer function called with filename: " + filename)

# The god of creation functions
# This is basically the same as the LMC GUI functions section, but for Python programs instead of LMC programs. The functions are the same, but they are for Python programs instead of LMC programs.

########################################################################################################################################
# Creates a new Python program file which will be a text file that is just read when by a python function to run the Python program    #
########################################################################################################################################


# The god of creation functions

def createpython(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new Python program file which will be a text file that is just read when by a python function to run the Python program
    print("Create Python Program button clicked")
    # Pop up a message box that says it was created successfully
    createpythonfile = entry.get()  # Get the value of the entry widget
    print(createpythonfile + "python.txt")


    # Create a new text file with the name of the entry widget
    with open("frostlang/" + createpythonfile + "python.txt", "a") as f:
       f.write("Welcome to FrostLang! This is your new Python program file. You can start coding here.")

    # Put the new text file in a text file called "pythonprograms.txt" that is a list of all the Python programs that have been created

    createpythonfile = createpythonfile + "python.txt"  # Add the .txt extension to the file name


    with open("pythonprograms.txt", "a") as f:
        f.write(createpythonfile + "\n")

    # Close the GUI window
    pythonlanguageguicreateprogramname.destroy()

def pythonlanguageguicreate():
    global pythonlanguageguicreateprogramname
    pythonlanguageguicreateprogramname = customtkinter.CTk()
    pythonlanguageguicreateprogramname.title("Create Python Program")
    pythonlanguageguicreateprogramname.geometry("300x200")
    entry = customtkinter.CTkEntry(pythonlanguageguicreateprogramname, placeholder_text="Enter Python Name")
    entry.grid(row=1, column=0, pady=20, padx=20)
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createpythonfile = customtkinter.CTkButton(pythonlanguageguicreateprogramname, text="Create Python Program", command=lambda:createpython(entry))
    createpythonfile.grid(row=2, column=0, padx=20, pady=20)
    pythonlanguageguicreateprogramname.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    messagebox.showinfo("Create Python Program", "Python Program file creater has opened successfully! Please enter the name of your new Python program file and click the Create Python Program button to create it.")

    pythonlanguageguicreateprogramname.mainloop()

####################################################################################################
# Deletes the text file that is the Python program file that was created by the create function    #
####################################################################################################

def deletepython(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new Python program file which will be a text file that is just read when by a python function to run the Python program
    print("Delete Python Program button clicked")
    # Pop up a message box that says it was deleted successfully
    deletepythonfile = entry.get()  # Get the value of the entry widget
    print(deletepythonfile + "python.txt")

    # Delete the text file with the name of the entry widget
    if os.path.exists("frostlang/" + deletepythonfile + "python.txt"):
      os.remove("frostlang/" + deletepythonfile + "python.txt")
      messagebox.showinfo("Delete Python Program", "Python Program file deleted successfully!")
    else:
        messagebox.showinfo("Delete Python Program", "Python Program file does not exist or could not be deleted!")

    # Remove the deleted text file from the "pythonprograms.txt" list of all the Python programs that have been created

    deletepythonfile = deletepythonfile + "python.txt"  # Add the .txt extension to the file name

    with open("pythonprograms.txt", "r") as f:
        lines = f.readlines()                           # Read all lines from the file
    with open("pythonprograms.txt", "w") as f:
        for line in lines:
            if line.strip() != deletepythonfile:           # If the line does not match the deleted file name, write it back to the file
                f.write(line)

    # Close the GUI window
    pythonlanguageguideleteprogramname.destroy()

def pythonlanguageguidelete():
    global pythonlanguageguideleteprogramname
    pythonlanguageguideleteprogramname = customtkinter.CTk()
    pythonlanguageguideleteprogramname.title("Delete Python Program")
    pythonlanguageguideleteprogramname.geometry("300x200")
    entry = customtkinter.CTkEntry(pythonlanguageguideleteprogramname, placeholder_text="Enter Python Program Name")
    entry.grid(row=1, column=0, pady=20, padx=20)
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createpythonfile = customtkinter.CTkButton(pythonlanguageguideleteprogramname, text="Delete Python Program", command=lambda:deletepython(entry))
    createpythonfile.grid(row=2, column=0, padx=20, pady=20)
    pythonlanguageguideleteprogramname.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    messagebox.showinfo("Delete Python Program", "Python Program file deleter has opened successfully! Please enter the name of your Python program file and click the Delete Python Program button to delete it.")

    pythonlanguageguideleteprogramname.mainloop()

#####################################################################################################
# Opens the text file that is the Python program file that was created by the create function       #
#####################################################################################################

def openpython(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new Python program file which will be a text file that is just read when by a python function to run the Python program
    print("Open Python Program button clicked")
    # Pop up a message box that says it was opened successfully
    openpythonfile = entry.get()  # Get the value of the entry widget
    print(openpythonfile)

    # Delete the text file with the name of the entry widget
    if os.path.exists("frostlang/" + openpythonfile + "python.txt"):
      os.remove("frostlang/" + openpythonfile + "python.txt")
      messagebox.showinfo("Open Python Program", "Python Program file opened successfully!")
      openpythonfile = openpythonfile + "python.txt"  # Add the .txt extension to the file name
      pythonfileviewer(openpythonfile)
    else:
        messagebox.showinfo("Open Python Program", "Python Program file does not exist or could not be opened!")

    # Close the GUI window
    pythonlanguageguiopenprogramname.destroy()

def pythonlanguageguiopen():
    global pythonlanguageguiopenprogramname
    pythonlanguageguiopenprogramname = customtkinter.CTk()
    pythonlanguageguiopenprogramname.title("Open Python Program")
    pythonlanguageguiopenprogramname.geometry("300x200")
    entry = customtkinter.CTkEntry(pythonlanguageguiopenprogramname, placeholder_text="Enter Python Program Name")
    entry.grid(row=1, column=0, pady=20, padx=20)
    #Creating an button
    #https://customtkinter.tomschimansky.com/tutorial/grid-system
    createpythonfile = customtkinter.CTkButton(pythonlanguageguiopenprogramname, text="Open Python Program", command=lambda:openpython(entry))
    createpythonfile.grid(row=2, column=0, padx=20, pady=20)
    pythonlanguageguiopenprogramname.grid_columnconfigure(0, weight=1)     #Sets the button in the middle of the GUI
    messagebox.showinfo("Open Python Program", "Python Program file opener has opened successfully! Please enter the name of your Python program file and click the Open Python Program button to open it.")

    pythonlanguageguiopenprogramname.mainloop()
