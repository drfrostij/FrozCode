###################################
#                                 #
#    Created By DrFrostij         #
#                                 #
###################################


########################
# The imports section  #
########################

# Run the LMC program
from lmcvariables import run_program as execute_lmc



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
# LMC Coding functions Section #
################################

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
    # This opens the text file with the name of the entry widget in a new window and lets user edit it
    # Open the text file with the name of the entry widget
    global lmcfileviewerwindowet
    lmcfileviewerwindowet = customtkinter.CTk()
    lmcfileviewerwindowet.title("LMC Program Viewer")
    lmcfileviewerwindowet.geometry("800x600")
    text_widget = customtkinter.CTkTextbox(lmcfileviewerwindowet)
    text_widget.pack(fill="both", expand=True)
    BASE_DIR = Path(__file__).resolve().parent
    with open(BASE_DIR / "frostlang" / openlmcfile, "r") as f:
        text_widget.insert("1.0", f.read())

    # This is the save button that saves the text file with the name of the entry widget
    save_button = customtkinter.CTkButton(lmcfileviewerwindowet, text="Save", command=lambda: save_lmc_file(openlmcfile, text_widget))
    save_button.pack(pady=10)

    # This is the run button that runs the LMC program in the text file with the name of the entry widget
    run_button = customtkinter.CTkButton( lmcfileviewerwindowet, text="Run", command=lambda: run_program(text_widget.get("1.0", "end-1c")))
    run_button.pack(pady=10)
    lmcfileviewerwindowet.mainloop()



def save_lmc_file(openlmcfile, text_widget):
    # This function saves the text file with the name of the entry widget
    BASE_DIR = Path(__file__).resolve().parent
    with open(BASE_DIR / "frostlang" / openlmcfile, "w") as f:
        f.write(text_widget.get("1.0", "end-1c"))
    messagebox.showinfo("Save LMC Program", "LMC Program file saved successfully!")    


def run_program(program):
    # This function runs the LMC program in the text file with the name of the entry widget
    print("Running LMC Program...")
    # Here we will run the LMC program using the run_program function from lmcvariables.py
    # We will also display a message box that says it was run successfully
    #https://stackoverflow.com/questions/61468952/copying-text-from-a-txt-file-and-assigning-it-into-a-variable-in-python
    # Copying text from a txt file and assigning it into a variable in python
    # GUI to display the output of the LMC program in a new window
    global lmcoutputwindow
    lmcoutputwindow = customtkinter.CTkToplevel(lmcfileviewerwindowet)
    lmcoutputwindow.title("LMC Program Output")
    lmcoutputwindow.geometry("800x600")
    output_text = customtkinter.CTkTextbox(lmcoutputwindow)
    output_text.pack(fill="both", expand=True)
    # Run the LMC program using lmcvariables.py
    from lmcvariables import run_program as execute_lmc

    try:
        result = execute_lmc(program)
        output_text.insert("1.0", "LMC Program:\n\n")
        output_text.insert("end", program)
        output_text.insert("end", "\n\nLMC Output:\n\n")
        output_text.insert("end", result)
        messagebox.showinfo("Run LMC Program", "LMC Program ran successfully!")
    except Exception as error:
        output_text.insert("1.0", "LMC Program:\n\n")
        output_text.insert("end", program)
        output_text.insert("end", "\n\nLMC Error:\n\n")
        output_text.insert("end", str(error))
        messagebox.showerror("Run LMC Program", str(error))





##################################################################################################################################
# Creates a new LMC program file which will be a text file that is just read when by a python function to run the LMC program    #
##################################################################################################################################


# The god of creation functions

def createlmc(entry):
    # https://www.w3schools.com/python/python_file_write.asp
    # This function creates a new LMC program file which will be a text file that is just read when by a python function to run the LMC program
    print("Create LMC Program button clicked")
    # Get the value of the entry widget
    createlmcfile = entry.get()
    print(createlmcfile + "lmc.txt")
    # Create the frostlang folder if it doesn't exist
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FOLDER = os.path.join(BASE_DIR, "frostlang")
    os.makedirs(FOLDER, exist_ok=True)

    # Create a new text file with the name of the entry widget
    filename = createlmcfile + "lmc.txt"
    filepath = os.path.join(FOLDER, filename)
    with open(filepath, "a") as f:
        f.write("Welcome to FrostLang! This is your new LMC program file. You can start coding here.")

    # Put the new text file in a text file called "lmcprograms.txt" that is a list of all the LMC programs that have been created

    with open(os.path.join(BASE_DIR, "lmcprograms.txt"), "a") as f:
        f.write(filename + "\n")

    # Close the GUI window
    popup = messagebox.showinfo("Create LMC Program", "LMC Program file created successfully!")
    lmclanguageguicreateprogramname.after(200, lmclanguageguicreateprogramname.destroy)


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
    openlmcfile = openlmcfile + "lmc.txt"  # Add the .txt extension to the file name
    lmcfileviewer(openlmcfile)
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

# run the LMC program in the text file with the name of the entry widget

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

lmclanguagegui()