from algorithms.Algorithm import *


class HillClimbing(Algorithm):
    def __init__(self, initial_solution, max_iterations=10000, max_iterations_no_imp=1000):
        super().__init__(initial_solution, max_iterations, max_iterations_no_imp)

    def execute(self, calback, file = 'hill_climbing_5.json'):
        start = perf_counter()
        iteration = 0
        iteration_no_imp = 0
        solution = self.initial_solution
        evaluation = solution.evaluation

        self.open_file(file)
        self.write_to_file(file, solution)

        
        while not self.stop(iteration, iteration_no_imp):
            iteration += 1
            iteration_no_imp += 1

            neighbour = self.neighbour_solution(solution)
            neighbour_evaluation = neighbour.evaluation

            if (neighbour_evaluation > evaluation): 
                self.write_to_file(file, neighbour)
                solution = neighbour
                evaluation = neighbour_evaluation
                iteration_no_imp = 0

        elapsed = perf_counter() - start
        solution.time = elapsed
        self.close_file(file)

        calback(solution)
        return solution
