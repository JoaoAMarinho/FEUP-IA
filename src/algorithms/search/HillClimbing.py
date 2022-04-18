from time import perf_counter
from algorithms.Algorithm import Algorithm

class HillClimbing(Algorithm):
    def __init__(self, initial_solution, max_iterations=10000, max_iterations_no_imp=1000):
        super().__init__(initial_solution, max_iterations, max_iterations_no_imp)

        def execute(self):
            start = perf_counter()
            iteration = 0
            iteration_no_imp = 0

            solution = self.initial_solution
            evaluation = self.evaluate(solution)
            
            while not self.stop(iteration, iteration_no_imp):
                iteration += 1
                iteration_no_imp += 1

                neighbour = self.neighbour_solution(solution)
                neighbour_evaluation = self.evaluate(neighbour)

                if (neighbour_evaluation > evaluation): 
                    solution = neighbour
                    evaluation = neighbour_evaluation
                    iteration_no_imp = 0

            elapsed = perf_counter() - start

            return solution
