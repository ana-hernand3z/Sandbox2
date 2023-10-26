# ------------- INDEX ---------------
# __init__: Initialize program
# set_source_registers: sets data registers
# execute: performs operations in programs
# classify: performs classification
# calculate_fitness : calculates the program fitness
# print_program : prints program
# sort_program_by_fitness : returns fitness

import InstructionHelper as ihelper
from Config import config
import copy as copy
import numpy as np 

class Program:

    # Receives inputs and outputs
    def __init__(self, inputs: int, outputs: int):

        # Set the number of outputs if we're using GPR
        self.outputs = outputs + config.gpr

        self.target = [0] * self.outputs

        self.inputs = inputs
        self.source = [0] * self.inputs

        self.instruction_array = ihelper.generate_instructions(config.instruction_cout, self.inputs, self.outputs)
        self.fitness = 0
        self.instruction_cout = config.instruction_cout

        self.classes_identified = [0] * outputs
    
    # set_source_registers receives a data list and copies it into the Program
    def set_source_registers(self, data: list) -> None:
        # can also use list(data)
        self.source = copy.copy(data)
    
    # Calls helper and performs all operations
    def execute(self) -> None:
        ihelper.execute_instructions(self.instruction_array, self.source, self.target)
    
    # Once execution is completed, it receives the correct class and checks if the max value in the program matches the class
    def classify(self, classification: int) -> int:
        if (classification == np.argmax(self.target)):
            return 1
        return 0

    # Receives a score and keeps it 
    # Fitness keeps track of correct data
    def calculate_fitness(self, score: int) -> None:
        self.fitness = score
        
    def print_program(self):
        ihelper.print_instructions(self.instruction_array)

    # Returns fitness
    # Used for sorting 
    def sort_program_by_fitness(self):
        return self.fitness