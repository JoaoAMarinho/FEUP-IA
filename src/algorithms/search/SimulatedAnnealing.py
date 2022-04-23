from operator import ne
from numpy import exp, random
from algorithms.Algorithm import *


class SimulatedAnnealing(Algorithm):
    def __init__(self, initial_solution, max_iterations=10000, initial_temperature=100000, temperature_decrease_factor=0.5):
        super().__init__(initial_solution, max_iterations)
        self.initial_temp = initial_temperature
        self.temp_decrease_factor = temperature_decrease_factor

    def schedule_temperature(self, t):
        return t * self.temp_decrease_factor

    def write_to_file(self, file, solution, iteration):
        data = {'evaluation': solution.evaluation,
                'time': solution.time,
                'iteration': iteration,
                'temperature': solution.temp,
                'initial temperature': solution.initial_temp}

        with open(file, 'a') as outfile:
            outfile.write(json.dumps(data)+',\n')
            outfile.close()

    def execute(self, callback, file = 'simulated_annealing_5.json'):
        start = perf_counter()
        iteration = 0
        iteration_no_imp = 0

        solution = self.initial_solution
        evaluation = solution.evaluation
        temperature = self.initial_temp

        self.open_file(file)
        solution.time = perf_counter() - start
        solution.temp = temperature
        solution.initial_temp = self.initial_temp
        self.write_to_file(file, solution, iteration)

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
                neighbour.time = perf_counter() - start
                neighbour.temp = temperature
                neighbour.initial_temp = self.initial_temp
                solution = neighbour
                evaluation = neighbour_evaluation
                iteration_no_imp = 0
            self.write_to_file(file, solution, iteration)

        elapsed = perf_counter() - start
        self.close_file(file)
        solution.time = elapsed

        callback(solution)
        return solution
