from Instruction import Instruction as i
import numpy as np

# --------- INDEX -------------
# ** SINGLE INSTRUCTION HANDLE **
# random_instruction(int, int): generates random instruction
# execute_instruction(i, list, list): executes an instruction
# print_instructions(i): prints an instruction
# ** MULTIPLE INSTRUCTION HANDLE **
# generate_instruction(int, int, int): returns np.array of instructions

# ------- SINGLE INSTRUCTION HANDLE ------------
# Generates a random instruction
# Receives input and output
# Returns instruction
def random_instruction(inputs: int, outputs: int):
    mode = np.random.randint(0, 2)
    target = np.random.randint(0, outputs)
    operation = np.random.randint(0, 4) 
    source = np.random.randint(0, inputs)
    return i(mode, target, operation, source)

# Receives a single instruction, source registers and target registers and executes it
def execute_instruction(instruction: i, source: list, target: list) -> None:
    if(instruction.mode == 0):
        target[instruction.target] = instruction.perform_operation(target[instruction.target], target[instruction.source%len(target)])
    else:
        target[instruction.target] = instruction.perform_operation(target[instruction.target], source[instruction.source])

# Receives an instruction and prints it
def print_instruction(instruction: i) -> None:
    instruction.print_instruction()

# --------- MULTIPLE INSTRUCTION HANDLE -----------
# Receives count, insputs and outputs
# returns a numpy array of random_instructions
def generate_instructions(instruction_count: int, inputs: int, outputs: int) -> np.array:
    return np.array([random_instruction(inputs, outputs) for _ in range(instruction_count)], dtype=object)

def execute_instructions(instruction_array: np.array, source: list, target: list) -> None:
    vfunc = np.vectorize(execute_instruction, excluded=['source', 'target'])
    vfunc(instruction_array, source=source, target=target)

def print_instructions(instruction_array: np.array):
    vfunc = np.vectorize(print_instruction)
    vfunc(instruction_array)

