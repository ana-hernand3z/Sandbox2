import InstructionHelper as ihelper
import numpy as np
from Program import Program as p

def generate_program(inputs: int, outputs: int):
    return p(inputs, outputs)

def run_program(program: p, data: list, classification: int) -> int:
    program.set_source_registers(data)
    ihelper.execute_instructions(program.instruction_array, program.source, program.target)
    return program.classify(classification)

def set_program_score(program: p, score: int):
    program.calculate_fitness(score)

def generate_programs(inputs: int, outputs: int, program_cout: int):
    array = []
    for _ in range(program_cout):
        array.append(generate_program(inputs, outputs))
    return array
    
