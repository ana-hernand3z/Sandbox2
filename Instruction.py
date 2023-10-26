# Instructions will be in the form of:
# [Mode Target Operation Source]

# If mode == 1, then we use source
# If mode == 0, then we use register

# --------------- INDEX--------------------
# __init__ : Initialize Instruction
# perform_operation : do the instruction operation
# print_instruction : print current instruction

class Instruction:
    def __init__(self, mode:int, target:int, operator: int, source: int):
        self.mode = mode
        self.target = target
        self.operator = operator
        self.source = source

    # Performs the operation defined in the instruction. 
    # It receives the target and source data and returns float
    def perform_operation(self, target: float, source: float) -> float:
        if(self.operator == 0):
            return target + source
        if(self.operator == 1):
            return target - source
        if(self.operator == 2):
            if(self.mode == 1): return source*2
            return target*2
        if(self.operator==3):
            if(self.mode == 1): return source/2
            return target/2
    
    # Prints instruction
    def print_instruction(self) -> None:
        operations = {
            0 : '+',
            1 : '-',
            2 : '*',
            3 : '/'
        }
        s = ""
        if(self.mode == 1): s = "R"
        if(self.mode == 0): s = "x"
        if(self.operator >= 2): d = 2
        else: d = self.source 
        if(self.operator < 2):
            print(f'R[{self.target}] <- R[{self.target}] {operations[self.operator]} {s}[{d}]')
        else :
            print(f'R[{self.target}] <- R[{self.target}] {operations[self.operator]} {d}')
    