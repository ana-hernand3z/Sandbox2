from Program import Program as p
from Config import config
import random as r

data = [4, 5, 2.2, 3.4]
programs = [p(4, 3) for _ in range (1000)]

for c in programs:
    c.set_source_registers(data)
    c.execute()




