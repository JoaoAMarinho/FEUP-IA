from operator import ne
from numpy import exp, random
from algorithms.Algorithm import *


class SimulatedAnnealing(Algorithm):
    def __init__(self, initial_solution, max_iterations=10000, initial_temperature=1000, temperature_decrease_factor=0.9):
        super().__init__(initial_solution, max_iterations)
        self.initial_temp = initial_temperature
        self.temp_decrease_factor = temperature_decrease_factor

    def schedule_temperature(self, t):
        return t * self.temp_decrease_factor

    def execute(self, file):
        start = perf_counter()
        iteration = 0
        iteration_no_imp = 0

        solution = self.initial_solution
        evaluation = solution.evaluation
        temperature = self.initial_temp

        self.open_file(file)

        self.write_to_file(file, solution)

        while not self.stop(iteration, iteration_no_imp):
            iteration += 1
            iteration_no_imp += 1

            temperature = self.schedule_temperature(temperature)
            if temperature == 0:
                return solution

            neighbour = self.neighbour_solution(solution)
            neighbour_evaluation = neighbour.evaluation
            delta_evaluation = neighbour_evaluation - evaluation

            if delta_evaluation > 0 or random.uniform(0.0, 1.0) <= exp(delta_evaluation/temperature):
                self.write_to_file(file,neighbour)
                solution = neighbour
                evaluation = neighbour_evaluation
                iteration_no_imp = 0

        elapsed = perf_counter() - start
        self.close_file(file)
        solution.time = elapsed
        return solution
