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
from tkinter import simpledialog

##########################
# Main Startup Code Area #
##########################


# Little Man Computer (LMC) Interpreter

variables = {}

# LMC Memory
memory = [0] * 100

# LMC Registers
accumulator = 0
program_counter = 0

# LMC Output
output = []


def run_program(code, input_values=None):
    global variables, memory, accumulator, program_counter, output

    # Reset all variables before running the program
    variables = {}
    memory = [0] * 100
    accumulator = 0
    program_counter = 0
    output = []

    if input_values is None:
        input_values = []

    input_position = 0

    # LMC Commands
    commands = [
        "INP", "OUT", "LDA", "STA",
        "ADD", "SUB", "BRA", "BRZ",
        "BRP", "HLT", "DAT"
    ]

    # Remove empty lines and comments
    lines = []

    for line in code.splitlines():
        line = line.split(";")[0].strip()

        if line:
            lines.append(line)

    # Check program size
    if len(lines) > 100:
        raise ValueError("LMC programs cannot exceed 100 memory locations.")

    # Store program instructions
    program = []
    labels = {}

    # First pass: Identify labels
    for address, line in enumerate(lines):
        parts = line.split()

        if parts[0].upper() not in commands:
            label = parts.pop(0).upper()
            labels[label] = address

        if not parts:
            raise SyntaxError(f"Missing instruction at address {address}")

        command = parts[0].upper()
        argument = parts[1] if len(parts) > 1 else None

        if command not in commands:
            raise SyntaxError(f"Unknown command: {command}")

        program.append((command, argument))

    # Second pass: Load DAT values into memory
    for address, (command, argument) in enumerate(program):
        if command == "DAT":
            if argument is not None:
                memory[address] = int(argument)

    # Start executing the program
    running = True
    instruction_count = 0

    while running:

        if program_counter >= len(program):
            raise RuntimeError("Program counter exceeded program length.")

        # Prevent infinite loops
        instruction_count += 1

        if instruction_count > 10000:
            raise RuntimeError("Program exceeded the instruction limit.")

        command, argument = program[program_counter]

        # Move to the next instruction
        next_instruction = program_counter + 1

        # INP - Input a number into the accumulator
        # INP - Input a number into the accumulator
        if command == "INP":
            value = simpledialog.askinteger("LMC Input","Enter a number:")
            if value is None:
                raise RuntimeError("Program input cancelled.")

            accumulator = value

        # OUT - Output the accumulator
        elif command == "OUT":
            output.append(str(accumulator))

        # LDA - Load a value into the accumulator
        elif command == "LDA":
            address = labels[argument.upper()]
            accumulator = memory[address]

        # STA - Store the accumulator in memory
        elif command == "STA":
            address = labels[argument.upper()]
            memory[address] = accumulator

        # ADD - Add a value to the accumulator
        elif command == "ADD":
            address = labels[argument.upper()]
            accumulator += memory[address]

        # SUB - Subtract a value from the accumulator
        elif command == "SUB":
            address = labels[argument.upper()]
            accumulator -= memory[address]

        # BRA - Branch always
        elif command == "BRA":
            next_instruction = labels[argument.upper()]

        # BRZ - Branch if accumulator is zero
        elif command == "BRZ":
            if accumulator == 0:
                next_instruction = labels[argument.upper()]

        # BRP - Branch if accumulator is positive or zero
        elif command == "BRP":
            if accumulator >= 0:
                next_instruction = labels[argument.upper()]

        # HLT - Stop the program
        elif command == "HLT":
            running = False

        # DAT - Data storage, not an executable instruction
        elif command == "DAT":
            raise RuntimeError("Attempted to execute a DAT instruction.")

        program_counter = next_instruction

    return "\n".join(output)

