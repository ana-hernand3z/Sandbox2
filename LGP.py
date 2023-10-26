# Mode = 1 will be generations
# Mode = 0 will be accuracy

# ------------- INDEX ------------
# __init__ : initialize the genetic program
# run
# init_generations : when generation is 0, it runs it
import ProgramHelper as phelper
from Program import Program as p

import copy
import numpy as np
import random as r
from Config import config


class LGP:
    # Initialize class
    # Begin setting inputs and outputs
    # Generate population
    # Set data, accuracy, mode and initialize generation
    # Set the number of parents and children
    # Initialize data analytics arrays
    def __init__(self, inputs: int, outputs: int, number_of_programs: int, training_data: list, testing_data: list, accuracy: float, max_generation: int, mode: int):
        self.inputs = inputs 
        self.outputs = outputs
        
        # Initialize population
        self.population = copy.deepcopy(phelper.generate_programs(self.inputs, self.outputs, number_of_programs))
        self.population_size = len(self.population)
        self.training_data = training_data
        self.testing_data = testing_data
        self.desired_accuracy = accuracy
        self.max_generation = max_generation
        self.generation = 0
        self.mode = mode
        # Set the size of the parents and the children
        self.parent_population_size = int((100-config.gap)*number_of_programs/100)
        self.children_population_size = int((config.gap)*number_of_programs/100)

        # Data Analytics
        self.best_scores = []
        self.worst_scores = []
        self.average_scores = []
        self.classes_identified = [0] * outputs
        self.classes_per_generation = []
        self.instructions_of_the_best = []
        self.instructions_of_the_worst = []

        self.run()
    
    def run(self) -> None:
        performance = 0
        while((self.mode == 1 and self.generation <= self.max_generation) or (self.mode == 0 and self.desired_accuracy != performance)):
            if(self.generation == 0):
                self.init_generations()
            self.train(self.parent_population_size, self.population_size)
            self.population.sort(key=p.sort_program_by_fitness, reverse = True)
            self.fetch_scores()
            self.replace_children()
            performance = self.best_scores[self.generation]/len(self.training_data)*100
            print("Generation %d best performance: %d" %(self.generation, performance))
            self.generation += 1
            

    def init_generations(self) -> None:
        self.train(0, len(self.population))
        self.population.sort(key=p.sort_program_by_fitness, reverse = True)
        self.fetch_scores()
        self.generation += 1

    def train(self, fr: int, to: int) -> None:
        for c in range(fr, to):
            score = 0
            for d in self.training_data:
                try:
                    result =  phelper.run_program(self.population[c], d[:self.inputs], d[self.inputs])
                    if(result):
                        self.population[c].classes_identified[int(d[self.inputs])] += 1
                        self.classes_identified[int(d[self.inputs])] += 1
                    score += result
                except OverflowError:
                    print("Overflow error")
                    score = 0
            self.population[c].calculate_fitness(score)
    
    # Fill score arrays from best to average
    def fetch_scores(self) -> None:
        self.best_scores.append(self.population[0].fitness)
        self.worst_scores.append(self.population[len(self.population)-1].fitness)
    
    def replace_children(self) -> None:
        sample_population = r.sample(self.population[0:self.parent_population_size], self.children_population_size)
        self.replace_with_parents(sample_population)
    
    # replace children with sampled parents
    def replace_with_parents(self, parents: list) -> None:
        j = 0
        for c in range(self.parent_population_size, len(self.population)):
            self.population[c] = copy.deepcopy(parents[j])
            j += 1